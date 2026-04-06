"""ComInc. AI Agent System — CLI entry point.

Usage:
    python -m src.main
    python -m src.main "新しい予約が入った"
    python -m src.main --agent marketing "SEO audit cominc.co"
"""

import os
import sys

os.environ.setdefault("PYTHONIOENCODING", "utf-8")

from dotenv import load_dotenv
load_dotenv(override=True)

import anyio

from claude_agent_sdk import query, ClaudeAgentOptions, ResultMessage, SystemMessage

from src.orchestrator import get_orchestrator_config, build_agent_definitions
from src.agents.base import get_agent_mcp


# ---------------------------------------------------------------------------
# Shared streaming helper — DRY: one place for message handling
# ---------------------------------------------------------------------------
async def _stream_response(prompt: str, options: ClaudeAgentOptions) -> None:
    """Stream query results to stdout."""
    async for message in query(prompt=prompt, options=options):
        if isinstance(message, ResultMessage):
            print(message.result)
            if message.stop_reason == "end_turn":
                print("\n✅ Task completed.")
        elif isinstance(message, SystemMessage) and message.subtype == "init":
            session_id = message.data.get("session_id")
            if session_id:
                print(f"Session: {session_id}\n")


# ---------------------------------------------------------------------------
# Run modes
# ---------------------------------------------------------------------------
async def run_orchestrator(user_input: str) -> None:
    """Send a task to the CEO Orchestrator (Ottar)."""
    config = get_orchestrator_config()

    print(f"\n🏢 ComInc. Orchestrator (Ottar)")
    print(f"📝 Task: {user_input}\n")
    print("-" * 60)

    await _stream_response(
        prompt=user_input,
        options=ClaudeAgentOptions(
            system_prompt=config["system_prompt"],
            agents=config["agents"],
            mcp_servers=config["mcp_servers"],
            allowed_tools=config["allowed_tools"],
            max_turns=config["max_turns"],
            permission_mode="default",
        ),
    )
    print("-" * 60)


async def run_single_agent(agent_name: str, user_input: str) -> None:
    """Run a single specialist agent directly (bypass Ottar)."""
    agents = build_agent_definitions()
    if agent_name not in agents:
        print(f"❌ Unknown agent: {agent_name}")
        print(f"Available: {', '.join(agents.keys())}")
        return

    agent_def = agents[agent_name]
    print(f"\n🤖 {agent_name}")
    print(f"📝 Task: {user_input}\n")
    print("-" * 60)

    await _stream_response(
        prompt=user_input,
        options=ClaudeAgentOptions(
            system_prompt=agent_def.prompt,
            allowed_tools=agent_def.tools,
            mcp_servers=get_agent_mcp(agent_name),
            permission_mode="default",
        ),
    )


async def interactive_mode() -> None:
    """Interactive CLI loop — Sho types commands, Ottar routes them."""
    agents = build_agent_definitions()
    agent_names = ", ".join(agents.keys())

    print("=" * 60)
    print("  ComInc. AI Agent System v0.2")
    print(f"  Orchestrator: ottar")
    print(f"  Team: {agent_names}")
    print("  Type your instruction. 'quit' to exit.")
    print("  Use '@agent_name message' to talk directly to an agent.")
    print("=" * 60)

    while True:
        try:
            user_input = input("\n💬 Sho > ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nさようなら！")
            break

        if not user_input:
            continue
        if user_input.lower() in ("quit", "exit", "q"):
            print("さようなら！")
            break

        # Direct agent access: @cat do SEO audit
        if user_input.startswith("@"):
            parts = user_input[1:].split(" ", 1)
            if len(parts) == 2:
                await run_single_agent(parts[0], parts[1])
            else:
                print(f"Usage: @agent_name your message")
                print(f"Agents: {agent_names}")
            continue

        await run_orchestrator(user_input)


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------
def main():
    args = sys.argv[1:]

    if "--pipeline" in args:
        idx = args.index("--pipeline")
        pipeline_name = args[idx + 1] if idx + 1 < len(args) else None
        if pipeline_name == "sns":
            from src.pipelines.sns_pipeline import run_sns_pipeline
            anyio.run(run_sns_pipeline)
        elif pipeline_name == "sns-schedule":
            from src.pipelines.sns_pipeline import run_sns_scheduling
            anyio.run(run_sns_scheduling)
        elif pipeline_name == "sns-factcheck":
            from src.pipelines.sns_pipeline import run_sns_factcheck
            anyio.run(run_sns_factcheck)
        elif pipeline_name == "sns-publish":
            from src.pipelines.sns_pipeline import run_sns_publish_threads
            anyio.run(run_sns_publish_threads)
        elif pipeline_name == "sns-auto":
            from src.pipelines.sns_pipeline import run_sns_autopost
            anyio.run(run_sns_autopost)
        elif pipeline_name == "sns-series":
            from src.pipelines.sns_pipeline import run_threads_series_post
            anyio.run(run_threads_series_post)
        else:
            print(f"Unknown pipeline: {pipeline_name}")
            print("Available: sns, sns-schedule, sns-factcheck, sns-publish, sns-auto, sns-series")
            sys.exit(1)
    elif "--agent" in args:
        idx = args.index("--agent")
        agent_name = args[idx + 1] if idx + 1 < len(args) else None
        task = " ".join(args[idx + 2:]) if idx + 2 < len(args) else None
        if not agent_name or not task:
            print("Usage: python -m src.main --agent <name> <task>")
            sys.exit(1)
        anyio.run(run_single_agent, agent_name, task)
    elif args:
        anyio.run(run_orchestrator, " ".join(args))
    else:
        anyio.run(interactive_mode)


if __name__ == "__main__":
    main()
