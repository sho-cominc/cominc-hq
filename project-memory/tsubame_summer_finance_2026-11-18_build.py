# -*- coding: utf-8 -*-
"""燕ハイランドロッジ 夏季営業 損益分岐ひな形（.xlsx）を作るスクリプト
作成: 2026-11-18 / Fin（T06）
使い方: python tsubame_summer_finance_2026-11-18_build.py [出力先.xlsx] [--sample]
  --sample は数式の検算用に「架空のテスト値」を入れる（実数ではない。保存版には使わない）
入力値はすべて空欄。ホテル固有の数字は Sho／オーナーの回答（project_tsubame_summer.md §6）で埋める。
"""
import sys
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.worksheet.datavalidation import DataValidation

OUT = sys.argv[1] if len(sys.argv) > 1 and not sys.argv[1].startswith("--") else "tsubame_summer_finance_2026-11-18.xlsx"
SAMPLE = "--sample" in sys.argv

SC = ["D", "E", "F"]  # 保守 / 基本 / 強気
INPUT_FILL = PatternFill("solid", fgColor="FFF2CC")
HEAD_FILL = PatternFill("solid", fgColor="D9E1F2")
SEC_FILL = PatternFill("solid", fgColor="E2EFDA")
BOLD = Font(bold=True)
thin = Side(style="thin", color="BFBFBF")
BOX = Border(left=thin, right=thin, top=thin, bottom=thin)

# (key, 項目, 単位, 形式, 確認先/メモ, サンプル値[保守,基本,強気]) — サンプルは検算専用の架空値
INPUTS = [
    ("SEC", "共通"),
    ("days", "夏季営業日数", "日", "0", "Q1 営業期間", [60, 75, 90]),
    ("weeks", "イベント開催回数（週1回なら営業週数）", "回", "0", "Q1・Q5", [8, 10, 12]),
    ("SEC", "① 宿泊"),
    ("rooms", "販売可能客室数", "室", "0", "Q1", [20, 20, 20]),
    ("occ", "稼働率（イベント効果を除く）", "%", "0.0%", "Q7 過去実績・T07 競合", [0.25, 0.35, 0.45]),
    ("adr", "ADR（1室1泊・税抜・入湯税除く）", "円", "#,##0", "Q1 → T12 料金案（料金は Sho／オーナーが決定）", [12000, 15000, 18000]),
    ("ppr", "1室あたり平均宿泊人数", "人", "0.0", "Q7", [2, 2, 2.2]),
    ("ota_share", "OTA 経由の予約比率", "%", "0.0%", "Q7・Q10", [0.7, 0.6, 0.5]),
    ("ota_fee", "OTA 手数料率（税抜売上に対して）", "%", "0.0%", "各 OTA の契約書", [0.12, 0.12, 0.12]),
    ("pay_fee", "決済手数料率（直販・現地決済分の平均）", "%", "0.0%", "決済会社の契約", [0.03, 0.03, 0.03]),
    ("v_room", "1室泊あたり変動費（清掃・リネン・アメニティ・光熱の変動分）", "円", "#,##0", "Q8・清掃の委託条件", [3000, 3000, 3000]),
    ("anc", "宿泊者1人あたり付帯売上（食事・売店）", "円", "#,##0", "Q1（食事提供の有無）", [2000, 2500, 3000]),
    ("anc_m", "付帯売上の粗利率", "%", "0.0%", "仕入・原価", [0.6, 0.6, 0.6]),
    ("SEC", "① 夏季の固定費（シーズン合計・税抜）"),
    ("fc_staff", "人件費（稼働に関係なくかかる分）", "円", "#,##0", "Q8", [3000000, 3500000, 4000000]),
    ("fc_util", "光熱費（基本料・最低限の空調/給湯など固定分）", "円", "#,##0", "過去の夏の請求書", [400000, 450000, 500000]),
    ("fc_clean", "清掃（委託の基本料など固定分）", "円", "#,##0", "清掃委託の条件", [200000, 200000, 200000]),
    ("fc_open", "開館費用（点検・水道開栓・修繕・備品・準備）", "円", "#,##0", "オーナー・施設担当", [500000, 500000, 500000]),
    ("fc_sys", "予約システム・OTA 固定費・通信", "円", "#,##0", "契約", [100000, 100000, 100000]),
    ("fc_promo", "宿泊の広告宣伝（シーズン）", "円", "#,##0", "Q3 予算", [200000, 300000, 400000]),
    ("fc_ins", "施設保険（夏季分）", "円", "#,##0", "保険証券", [100000, 100000, 100000]),
    ("fc_other", "その他固定費（夏季分の減価償却・リース等を含めるかは Sho と決める）", "円", "#,##0", "オーナー", [0, 0, 0]),
    ("SEC", "② 週替わりイベント（1回あたり・税抜）"),
    ("att", "来場者数", "人/回", "#,##0", "T04 事例・Q4 駐車台数が上限", [150, 300, 500]),
    ("trucks", "キッチンカー出店台数", "台/回", "0", "Q5", [3, 4, 6]),
    ("f_buy", "来場者のうちキッチンカーで買う人の割合", "%", "0.0%", "T04 事例", [0.7, 0.8, 0.85]),
    ("f_spend", "キッチンカー購入者の平均客単価", "円", "#,##0", "出店者への聞き取り（T13）", [1200, 1400, 1600]),
    ("fee_flat", "出店料モデルB: 定額（1台1回）", "円", "#,##0", "Q5・T13（取り決めは Sho／オーナー）", [5000, 5000, 5000]),
    ("fee_pct", "出店料モデルC: 売上歩合", "%", "0.0%", "Q5・T13", [0.1, 0.1, 0.1]),
    ("model", "採用する出店料モデル（1=A 無料 / 2=B 定額 / 3=C 歩合）", "-", "0", "シナリオ比較用。決定は Sho／オーナー", [1, 2, 3]),
    ("entry", "入場料（1人・通常は 0）", "円", "#,##0", "Sho／オーナー", [0, 0, 0]),
    ("d_buy", "自社ドリンク・物販の購入率", "%", "0.0%", "T04 事例", [0.3, 0.4, 0.5]),
    ("d_spend", "自社ドリンク・物販の客単価", "円", "#,##0", "メニュー案", [700, 800, 1000]),
    ("d_margin", "自社ドリンク・物販の粗利率", "%", "0.0%", "仕入・原価（酒類は許可が前提 → T05）", [0.6, 0.6, 0.6]),
    ("staff_n", "イベント当日のスタッフ人数", "人", "0", "Q8", [3, 4, 5]),
    ("staff_h", "1人あたり勤務時間", "時間", "0.0", "Q8", [6, 6, 6]),
    ("wage", "時給（法定福利・交通費込みの会社負担額）", "円", "#,##0", "Q8", [1300, 1300, 1300]),
    ("equip", "機材レンタル（テント・発電機・照明・音響など）", "円/回", "#,##0", "Q5（電源・水の有無）", [30000, 30000, 40000]),
    ("ins_ev", "イベント保険（1回ごとに掛ける場合）", "円/回", "#,##0", "T05 Law・保険会社の見積", [5000, 5000, 5000]),
    ("promo_ev", "告知費（1回あたり）", "円/回", "#,##0", "Q3", [10000, 10000, 15000]),
    ("misc_ev", "その他（仮設トイレ・ごみ・電気水道・駐車誘導・警備）", "円/回", "#,##0", "Q4・Q5", [20000, 25000, 30000]),
    ("SEC", "② イベントのシーズン費用（合計・税抜）"),
    ("ev_init", "初期費用（機材購入・看板・備品）", "円", "#,##0", "Q3", [200000, 200000, 300000]),
    ("ev_ins_s", "イベント保険（年・シーズン契約の場合。1回ごとと二重に入れない）", "円", "#,##0", "T05", [0, 0, 0]),
    ("ev_promo_s", "シーズン告知（ポスター・広告・冬の館内告知物の印刷）", "円", "#,##0", "Q3・T09", [100000, 150000, 200000]),
    ("SEC", "③ イベントによる追加宿泊"),
    ("conv", "来場者のうち『イベントがあるから泊まる』人の割合（増分のみ）", "%", "0.0%", "冬のアンケート（T08）・T04 事例", [0.01, 0.03, 0.05]),
    ("ev_ppr", "その宿泊者の1室あたり人数", "人", "0.0", "", [2, 2, 2.5]),
    ("ev_nights", "イベント1回あたり追加宿泊を受けられる夜数（前夜・当夜など）", "泊", "0", "イベントの曜日・時間", [1, 1, 2]),
    ("SEC", "⑤ 山頂のかき氷＋コーヒースタンド（ホテルが自分で売る）"),
    ("st_days", "スタンド営業日数（シーズン）", "日", "0", "Q1・天候・アクセス", [40, 50, 60]),
    ("st_months", "かき氷機の契約月数（夏だけのレンタルなら夏の月数／5年リースなら 12）", "か月", "0", "見積書（リースは中途解約不可が一般的 → 年12か月分を夏で回収）", [12, 12, 3]),
    ("ks_rent", "かき氷機の月額（税抜）", "円/月", "#,##0", "Sho の聞いた額『2万円台/月（約100万円クラス）』は未確認。見積で確定", [25000, 22000, 22000]),
    ("cf_rent", "コーヒー機材の月額（持ち込み・購入済みなら 0）", "円/月", "#,##0", "Sho", [0, 0, 0]),
    ("st_months_cf", "コーヒー機材の契約月数", "か月", "0", "Sho", [0, 0, 0]),
    ("ks_price", "かき氷 販売価格（税抜）", "円/杯", "#,##0", "Sho／オーナーが決定（T04 で相場）", [800, 1000, 1200]),
    ("ks_cost", "かき氷 1杯の原価（氷・シロップ・トッピング・カップ・スプーン）", "円/杯", "#,##0", "仕入見積", [200, 220, 250]),
    ("cf_price", "コーヒー 販売価格（税抜）", "円/杯", "#,##0", "Sho／オーナーが決定", [500, 600, 700]),
    ("cf_cost", "コーヒー 1杯の原価（豆・カップ・蓋・ミルク等）", "円/杯", "#,##0", "Sho（自分で淹れる）", [80, 90, 100]),
    ("ks_mix", "販売杯数のうち かき氷の割合", "%", "0.0%", "天候・気温で変わる", [0.5, 0.6, 0.6]),
    ("st_pay", "スタンドの決済手数料率（キャッシュレス分の平均）", "%", "0.0%", "決済会社", [0.03, 0.03, 0.03]),
    ("st_cups", "見込み販売杯数（1日・両方合計）", "杯/日", "#,##0", "T04 事例・山頂の人出（Q4）", [40, 80, 150]),
    ("st_staff_n", "スタンドの人数", "人", "0", "Sho 自身の時間を費用に入れるかも決める", [1, 1, 2]),
    ("st_staff_h", "1人あたり勤務時間", "時間", "0.0", "", [6, 6, 7]),
    ("st_wage", "時給（会社負担額。Sho の分も入れるなら単価を決める）", "円", "#,##0", "Q2（Sho の報酬）・Q8", [1300, 1300, 1300]),
    ("st_daily", "日々の固定費（氷・機材の運搬、発電機燃料/電気、水、ごみ）", "円/日", "#,##0", "Q4（山頂までの運搬手段・電源）", [3000, 3000, 4000]),
    ("st_init", "初期費用（許可の手数料・衛生設備・テント・看板・保冷・食品衛生責任者講習）", "円", "#,##0", "T05 Law・保健所", [150000, 150000, 200000]),
    ("SEC", "⑥ レストラン（Sho 側が運営）— 宿泊の付帯売上（anc）と重ねて数えない"),
    ("rs_days", "レストラン営業日数", "日", "0", "Q1", [60, 75, 90]),
    ("rs_covers", "1日あたり客数（宿泊者＋外来）", "人/日", "#,##0", "宿泊人数・来場者から置く", [20, 35, 50]),
    ("rs_check", "客単価（税抜）", "円", "#,##0", "メニュー案（価格は Sho が決定）", [2500, 3000, 3500]),
    ("rs_food", "食材原価率", "%", "0.0%", "メニュー原価", [0.35, 0.33, 0.32]),
    ("rs_pay", "決済手数料率", "%", "0.0%", "", [0.03, 0.03, 0.03]),
    ("rs_share", "John への支払い（レストラン売上に対する率）", "%", "0.0%", "Sho の説明 2026-11-18: 夏季のみ 25%（契約書未確認）", [0.25, 0.25, 0.25]),
    ("rs_labor", "レストラン人件費（シーズン）", "円", "#,##0", "Q8", [1200000, 1500000, 1800000]),
    ("rs_fixed", "レストランのその他固定費（シーズン。光熱の按分・機材・消耗品）", "円", "#,##0", "光熱費の按分方法も確認", [200000, 250000, 300000]),
    ("SEC", "⑥ 取り分の構造（夏季のみ。冬は別契約で対象外。Sho の説明 2026-11-18。定義は未確認 → スイッチで切り替え）"),
    ("p_sho", "ホテル純利益（NP）のうち Sho の取り分", "%", "0.0%", "Sho の説明 2026-11-18: 夏季のみ 20%（契約書未確認）", [0.2, 0.2, 0.2]),
    ("p_mgr", "NP のうち 支配人 Yukari の取り分", "%", "0.0%", "Sho の説明 2026-11-18: 夏季のみ 20%（契約書未確認）", [0.2, 0.2, 0.2]),
    ("p_own", "NP のうち オーナー John の取り分", "%", "0.0%", "Sho の説明 2026-11-18: 夏季のみ 60%（契約書未確認）", [0.6, 0.6, 0.6]),
    ("mgr_salary", "支配人 Yukari の給与（夏季分のみ。冬の給与は別契約で対象外。fc_staff には入れない）", "円", "#,##0", "オーナー・支配人", [1200000, 1200000, 1200000]),
    ("sw_salary", "支配人給与を NP の前に差し引くか（1=引く／0=引かない）", "-", "0", "定義の確認事項 D2", [1, 1, 1]),
    ("sw_rs_to", "レストランの 25% の行き先（1=John 個人へ／2=ホテルの NP に入る）", "-", "0", "D3", [1, 1, 1]),
    ("sw_stand", "山頂スタンドの区分（1=ホテル NP／2=Sho 側）", "-", "0", "D5", [1, 2, 2]),
    ("sw_event", "イベント（出店料・物販）の区分（1=ホテル NP／2=Sho 側）", "-", "0", "D5", [1, 1, 2]),
    ("sw_rs_base", "Sho 側に入れたスタンド・イベント売上にも 25% を払うか（1=払う／0=払わない）", "-", "0", "D5", [1, 1, 0]),
    ("sw_loss", "NP が赤字のとき（1=三者で同率負担／0=オーナーが全額負担し、Sho・支配人は 0）", "-", "0", "D1", [0, 0, 0]),
    ("p_side_sho", "Sho 側の利益のうち Sho 本人の取り分", "%", "0.0%", "D4（相手と率は未確認）", [1, 1, 1]),
]

wb = Workbook()
ws = wb.active
ws.title = "入力"
ws["A1"] = "燕ハイランドロッジ 夏季営業 — 入力値（黄色セルを埋める。金額は税抜）"
ws["A1"].font = Font(bold=True, size=13)
ws["A2"] = "作成 2026-11-18 Fin（T06）。ホテル固有の数字はまだ無いため全て空欄。Sho／オーナーの回答で埋める（出典と日付をH列に書く）。"
hdr = ["ID", "項目", "単位", "保守", "基本", "強気", "確認先（project_tsubame_summer.md §6 / タスク）", "出典・日付（埋めた人が書く）"]
for i, h in enumerate(hdr):
    c = ws.cell(row=4, column=i + 1, value=h)
    c.font = BOLD; c.fill = HEAD_FILL; c.border = BOX
R = {}
FMT = {}
r = 5
for item in INPUTS:
    if item[0] == "SEC":
        ws.cell(row=r, column=1, value=item[1]).font = BOLD
        for col in range(1, 9):
            ws.cell(row=r, column=col).fill = SEC_FILL
        r += 1
        continue
    key, label, unit, fmt, src, sample = item
    R[key] = r; FMT[key] = fmt
    ws.cell(row=r, column=1, value=key)
    ws.cell(row=r, column=2, value=label)
    ws.cell(row=r, column=3, value=unit)
    for j, col in enumerate(SC):
        c = ws[f"{col}{r}"]
        c.fill = INPUT_FILL; c.number_format = fmt; c.border = BOX
        if SAMPLE:
            c.value = sample[j]
    ws.cell(row=r, column=7, value=src)
    r += 1
dv = DataValidation(type="whole", operator="between", formula1="1", formula2="3", allow_blank=True)
ws.add_data_validation(dv)
for col in SC:
    dv.add(f"{col}{R['model']}")
ws.column_dimensions["A"].width = 11
ws.column_dimensions["B"].width = 58
ws.column_dimensions["C"].width = 7
for col in SC:
    ws.column_dimensions[col].width = 14
ws.column_dimensions["G"].width = 44
ws.column_dimensions["H"].width = 30
ws.freeze_panes = "D5"


def I(key, col):
    return f"入力!{col}{R[key]}"


# ---------- 計算シート ----------
cs = wb.create_sheet("計算")
cs["A1"] = "燕ハイランドロッジ 夏季営業 — 損益分岐（自動計算。入力シート以外は触らない）"
cs["A1"].font = Font(bold=True, size=13)
cs["A2"] = "空欄の入力は 0 として計算される。割り算ができない欄は空白表示。"
for i, h in enumerate(["ID", "項目", "単位", "保守", "基本", "強気", "式（記号）"]):
    c = cs.cell(row=4, column=i + 1, value=h)
    c.font = BOLD; c.fill = HEAD_FILL; c.border = BOX
C = {}
row = [5]


def sec(title):
    cs.cell(row=row[0], column=1, value=title).font = BOLD
    for col in range(1, 8):
        cs.cell(row=row[0], column=col).fill = SEC_FILL
    row[0] += 1


def calc(key, label, unit, fmt, f, note="", bold=False, safe=False):
    """f(col) -> Excel 式（= なし）"""
    rr = row[0]; C[key] = rr
    cs.cell(row=rr, column=1, value=key)
    cs.cell(row=rr, column=2, value=label).font = Font(bold=bold)
    cs.cell(row=rr, column=3, value=unit)
    for col in SC:
        expr = f(col)
        if safe:
            expr = f'IFERROR({expr},"")'
        c = cs[f"{col}{rr}"]
        c.value = "=" + expr
        c.number_format = fmt; c.border = BOX
        if bold:
            c.font = BOLD
    cs.cell(row=rr, column=7, value=note)
    row[0] += 1


def K(key, col):
    return f"{col}{C[key]}"


Y = "#,##0;[Red]-#,##0"
P = "0.0%"

sec("① 宿泊（イベントなし）")
calc("avail", "販売可能室泊", "室泊", "#,##0", lambda c: f"{I('rooms',c)}*{I('days',c)}", "rooms × days")
calc("rn", "稼働室泊", "室泊", "#,##0", lambda c: f"{K('avail',c)}*{I('occ',c)}", "avail × occ")
calc("rev_room", "宿泊売上", "円", Y, lambda c: f"{K('rn',c)}*{I('adr',c)}", "rn × ADR")
calc("fee_rate", "販売手数料率（実効）", "%", P, lambda c: f"{I('ota_share',c)}*{I('ota_fee',c)}+{I('pay_fee',c)}", "ota_share × ota_fee + pay_fee")
calc("anc_gp_rn", "1室泊あたり付帯粗利", "円", Y, lambda c: f"{I('ppr',c)}*{I('anc',c)}*{I('anc_m',c)}", "ppr × anc × anc_m")
calc("cm_rn", "1室泊あたり限界利益", "円", Y, lambda c: f"{I('adr',c)}*(1-{K('fee_rate',c)})-{I('v_room',c)}+{K('anc_gp_rn',c)}", "ADR×(1−fee) − v_room + 付帯粗利", bold=True)
calc("cm_total", "限界利益合計", "円", Y, lambda c: f"{K('rn',c)}*{K('cm_rn',c)}", "rn × cm_rn")
fc_keys = ["fc_staff", "fc_util", "fc_clean", "fc_open", "fc_sys", "fc_promo", "fc_ins", "fc_other"]
calc("fc", "夏季固定費合計", "円", Y, lambda c: "+".join(I(k, c) for k in fc_keys), "FC = Σ fc_*", bold=True)
calc("pl_room", "宿泊損益（イベントなし）", "円", Y, lambda c: f"{K('cm_total',c)}-{K('fc',c)}", "cm_total − FC", bold=True)
calc("be_rn", "損益分岐 室泊", "室泊", "#,##0", lambda c: f'IF({K("cm_rn",c)}<=0,"限界利益≦0",{K("fc",c)}/{K("cm_rn",c)})', "FC ÷ cm_rn", safe=True)
calc("be_occ", "損益分岐 稼働率", "%", P, lambda c: f"{K('be_rn',c)}/{K('avail',c)}", "be_rn ÷ avail（100%超なら今の ADR では届かない）", bold=True, safe=True)
calc("be_adr", "損益分岐 ADR（入力の稼働率のとき）", "円", "#,##0", lambda c: f"({K('fc',c)}/{K('rn',c)}+{I('v_room',c)}-{K('anc_gp_rn',c)})/(1-{K('fee_rate',c)})", "(FC÷rn + v_room − 付帯粗利) ÷ (1−fee)", bold=True, safe=True)

sec("② イベント 1回あたり（出店料モデル別）")
calc("truck_sales", "キッチンカー売上合計", "円/回", Y, lambda c: f"{I('att',c)}*{I('f_buy',c)}*{I('f_spend',c)}", "att × f_buy × f_spend")
calc("truck_sales_1", "キッチンカー1台あたり売上", "円/台", Y, lambda c: f"{K('truck_sales',c)}/{I('trucks',c)}", "÷ trucks（出店者が来てくれる水準かの目安）", safe=True)
calc("fee_A", "出店料収入 A 無料", "円/回", Y, lambda c: "0", "0")
calc("fee_B", "出店料収入 B 定額", "円/回", Y, lambda c: f"{I('trucks',c)}*{I('fee_flat',c)}", "trucks × fee_flat")
calc("fee_C", "出店料収入 C 歩合", "円/回", Y, lambda c: f"{K('truck_sales',c)}*{I('fee_pct',c)}", "truck_sales × fee_pct")
calc("vend_B", "出店者の手取り/台（B 定額・出店者の原価前）", "円/台", Y, lambda c: f"{K('truck_sales_1',c)}-{I('fee_flat',c)}", "出店者が続けられるかの確認用", safe=True)
calc("vend_C", "出店者の手取り/台（C 歩合・出店者の原価前）", "円/台", Y, lambda c: f"{K('truck_sales_1',c)}*(1-{I('fee_pct',c)})", "", safe=True)
calc("entry_rev", "入場料収入", "円/回", Y, lambda c: f"{I('att',c)}*{I('entry',c)}", "att × entry")
calc("drink_gp", "自社ドリンク・物販 粗利", "円/回", Y, lambda c: f"{I('att',c)}*{I('d_buy',c)}*{I('d_spend',c)}*{I('d_margin',c)}", "att × d_buy × d_spend × d_margin")
calc("ev_labor", "人件費", "円/回", Y, lambda c: f"{I('staff_n',c)}*{I('staff_h',c)}*{I('wage',c)}", "staff_n × staff_h × wage")
calc("ev_cost", "1回あたり費用合計", "円/回", Y, lambda c: f"{K('ev_labor',c)}+{I('equip',c)}+{I('ins_ev',c)}+{I('promo_ev',c)}+{I('misc_ev',c)}", "人件費 + 機材 + 保険 + 告知 + その他", bold=True)
for m, lab in [("A", "A 無料"), ("B", "B 定額"), ("C", "C 歩合")]:
    calc(f"ev_pl_{m}", f"1回あたり損益 {lab}", "円/回", Y,
         lambda c, m=m: f"{K('fee_'+m,c)}+{K('entry_rev',c)}+{K('drink_gp',c)}-{K('ev_cost',c)}",
         "出店料 + 入場料 + 物販粗利 − 費用", bold=True)
calc("per_head_AB", "来場者1人あたり貢献（A・B）", "円/人", Y, lambda c: f"{I('entry',c)}+{I('d_buy',c)}*{I('d_spend',c)}*{I('d_margin',c)}", "entry + d_buy×d_spend×d_margin")
calc("per_head_C", "来場者1人あたり貢献（C）", "円/人", Y, lambda c: f"{K('per_head_AB',c)}+{I('f_buy',c)}*{I('f_spend',c)}*{I('fee_pct',c)}", "+ f_buy×f_spend×fee_pct")
calc("be_att_A", "損益分岐 来場者数 A 無料", "人/回", "#,##0", lambda c: f"{K('ev_cost',c)}/{K('per_head_AB',c)}", "ev_cost ÷ 1人あたり貢献", safe=True)
calc("be_att_B", "損益分岐 来場者数 B 定額", "人/回", "#,##0", lambda c: f"MAX(0,{K('ev_cost',c)}-{K('fee_B',c)})/{K('per_head_AB',c)}", "(ev_cost − 定額収入) ÷ 1人あたり貢献", safe=True)
calc("be_att_C", "損益分岐 来場者数 C 歩合", "人/回", "#,##0", lambda c: f"{K('ev_cost',c)}/{K('per_head_C',c)}", "", safe=True)

sec("② イベント シーズン合計（採用モデル）")
calc("ev_pl_sel", "1回あたり損益（採用モデル）", "円/回", Y, lambda c: f"CHOOSE({I('model',c)},{K('ev_pl_A',c)},{K('ev_pl_B',c)},{K('ev_pl_C',c)})", "入力の model で選ぶ", safe=True)
calc("ev_season_fc", "イベントのシーズン費用", "円", Y, lambda c: f"{I('ev_init',c)}+{I('ev_ins_s',c)}+{I('ev_promo_s',c)}", "ev_init + ev_ins_s + ev_promo_s")
calc("ev_pl_season", "イベント単体のシーズン損益", "円", Y, lambda c: f"N({K('ev_pl_sel',c)})*{I('weeks',c)}-{K('ev_season_fc',c)}", "ev_pl_sel × weeks − シーズン費用", bold=True)
calc("be_att_sel", "シーズン費用も回収する来場者数/回（採用モデル）", "人/回", "#,##0",
     lambda c: (f"MAX(0,{K('ev_cost',c)}+{K('ev_season_fc',c)}/{I('weeks',c)}-CHOOSE({I('model',c)},0,{K('fee_B',c)},0))"
                f"/CHOOSE({I('model',c)},{K('per_head_AB',c)},{K('per_head_AB',c)},{K('per_head_C',c)})"),
     "(ev_cost + シーズン費用÷weeks − 定額収入) ÷ 1人あたり貢献", safe=True)

sec("③ イベントによる追加宿泊（あり／なし）")
calc("add_rn_dem", "追加宿泊の需要/回", "室泊/回", "#,##0.0", lambda c: f"{I('att',c)}*{I('conv',c)}/{I('ev_ppr',c)}", "att × conv ÷ ev_ppr", safe=True)
calc("add_rn_cap", "受けられる空室/回", "室泊/回", "#,##0.0", lambda c: f"{I('rooms',c)}*(1-{I('occ',c)})*{I('ev_nights',c)}", "rooms × (1−occ) × ev_nights（イベント日も平均稼働と仮定）")
calc("add_rn", "追加宿泊 室泊（シーズン）", "室泊", "#,##0", lambda c: f"MIN(N({K('add_rn_dem',c)}),{K('add_rn_cap',c)})*{I('weeks',c)}", "MIN(需要, 空室) × weeks")
calc("cm_rn_ev", "追加宿泊1室泊あたり限界利益", "円", Y, lambda c: f"{I('adr',c)}*(1-{K('fee_rate',c)})-{I('v_room',c)}+{I('ev_ppr',c)}*{I('anc',c)}*{I('anc_m',c)}", "ev_ppr で付帯粗利を計算")
calc("add_pl", "追加宿泊の利益", "円", Y, lambda c: f"{K('add_rn',c)}*{K('cm_rn_ev',c)}", "add_rn × cm_rn_ev", bold=True)
calc("occ_with", "イベントありの稼働率", "%", P, lambda c: f"({K('rn',c)}+{K('add_rn',c)})/{K('avail',c)}", "", safe=True)

sec("⑤ 山頂スタンド（かき氷＋コーヒー）")
calc("ks_gp", "かき氷 1杯の粗利", "円/杯", Y, lambda c: f"{I('ks_price',c)}*(1-{I('st_pay',c)})-{I('ks_cost',c)}", "price×(1−pay) − 原価", bold=True)
calc("ks_gpr", "かき氷 粗利率", "%", P, lambda c: f"{K('ks_gp',c)}/{I('ks_price',c)}", "", safe=True)
calc("cf_gp", "コーヒー 1杯の粗利", "円/杯", Y, lambda c: f"{I('cf_price',c)}*(1-{I('st_pay',c)})-{I('cf_cost',c)}", "", bold=True)
calc("cf_gpr", "コーヒー 粗利率", "%", P, lambda c: f"{K('cf_gp',c)}/{I('cf_price',c)}", "", safe=True)
calc("mix_gp", "1杯あたり粗利（販売構成で加重）", "円/杯", Y, lambda c: f"{I('ks_mix',c)}*{K('ks_gp',c)}+(1-{I('ks_mix',c)})*{K('cf_gp',c)}", "mix×ks_gp + (1−mix)×cf_gp")
calc("st_rent_total", "機材の契約総額（シーズンに負担する分）", "円", Y, lambda c: f"{I('ks_rent',c)}*{I('st_months',c)}+{I('cf_rent',c)}*{I('st_months_cf',c)}", "月額 × 契約月数（リースなら 12 か月分）")
calc("st_labor_d", "人件費/日", "円/日", Y, lambda c: f"{I('st_staff_n',c)}*{I('st_staff_h',c)}*{I('st_wage',c)}", "")
calc("st_fc_d", "1日あたり固定費（機材・初期費用を営業日で割った分を含む）", "円/日", Y,
     lambda c: f"{K('st_labor_d',c)}+{I('st_daily',c)}+({K('st_rent_total',c)}+{I('st_init',c)})/{I('st_days',c)}", "人件費 + 日々の固定費 + (機材総額 + 初期費用) ÷ 営業日", safe=True)
calc("st_be_cups", "損益分岐 杯数/日（構成どおり）", "杯/日", "#,##0", lambda c: f"{K('st_fc_d',c)}/{K('mix_gp',c)}", "1日固定費 ÷ 加重粗利", bold=True, safe=True)
calc("st_be_ks_only", "損益分岐 杯数/日（かき氷だけ売る場合）", "杯/日", "#,##0", lambda c: f"{K('st_fc_d',c)}/{K('ks_gp',c)}", "", safe=True)
calc("st_be_rentonly", "機材代だけを回収する杯数/日（人件費を除く）", "杯/日", "#,##0", lambda c: f"({K('st_rent_total',c)}/{I('st_days',c)})/{K('mix_gp',c)}", "Sho が自分で立つ場合の目安", safe=True)
calc("st_rev", "スタンド売上（シーズン・税抜）", "円", Y, lambda c: f"{I('st_cups',c)}*{I('st_days',c)}*({I('ks_mix',c)}*{I('ks_price',c)}+(1-{I('ks_mix',c)})*{I('cf_price',c)})", "")
calc("st_pl", "スタンド損益（シーズン）", "円", Y, lambda c: f"{I('st_cups',c)}*{I('st_days',c)}*{K('mix_gp',c)}-N({K('st_fc_d',c)})*{I('st_days',c)}", "見込み杯数×日数×加重粗利 − 固定費", bold=True)

sec("④ 合計とシナリオ比較")
calc("tot_without", "夏季損益（イベントなし）", "円", Y, lambda c: f"{K('pl_room',c)}", "= pl_room", bold=True)
calc("tot_with", "夏季損益（イベントあり）", "円", Y, lambda c: f"{K('pl_room',c)}+{K('ev_pl_season',c)}+{K('add_pl',c)}", "pl_room + イベント単体 + 追加宿泊", bold=True)
calc("tot_all", "夏季損益（イベント＋山頂スタンド）", "円", Y, lambda c: f"{K('tot_with',c)}+{K('st_pl',c)}", "tot_with + st_pl", bold=True)
calc("ev_effect", "イベントの効果（差額）", "円", Y, lambda c: f"{K('tot_with',c)}-{K('tot_without',c)}", "イベント単体 + 追加宿泊", bold=True)
calc("be_occ_with", "損益分岐 稼働率（イベントあり。イベント由来の宿泊を含む）", "%", P,
     lambda c: f"(({K('fc',c)}-{K('ev_pl_season',c)})/{K('cm_rn',c)})/{K('avail',c)}",
     "(FC − イベント単体損益) ÷ cm_rn ÷ avail", bold=True, safe=True)
calc("rev_total", "夏季売上合計（イベントあり）", "円", Y,
     lambda c: (f"{K('rev_room',c)}+{K('add_rn',c)}*{I('adr',c)}+({K('rn',c)}*{I('ppr',c)}+{K('add_rn',c)}*{I('ev_ppr',c)})*{I('anc',c)}"
                f"+({K('entry_rev',c)}+{I('att',c)}*{I('d_buy',c)}*{I('d_spend',c)}+N(CHOOSE({I('model',c)},0,{K('fee_B',c)},{K('fee_C',c)})))*{I('weeks',c)}"),
     "宿泊 + 付帯 + イベント（入場料・物販売上・出店料）", safe=True)
calc("rev_total_all", "夏季売上合計（＋スタンド）", "円", Y, lambda c: f"N({K('rev_total',c)})+{K('st_rev',c)}", "")
calc("fc_all", "固定費合計（宿泊 + イベントのシーズン費用 + スタンド固定費）", "円", Y, lambda c: f"{K('fc',c)}+{K('ev_season_fc',c)}+N({K('st_fc_d',c)})*{I('st_days',c)}", "")
calc("alert", "判定", "-", "@",
     lambda c: f'IF({K("fc",c)}=0,"入力待ち",IF({K("rev_total_all",c)}<{K("fc_all",c)},"要注意: 売上が固定費を下回る",IF({K("tot_all",c)}<0,"赤字","黒字")))',
     "Fin の警告ルール: 売上 < 固定費 → Sho に通知", bold=True)

sec("⑥ レストラン（Sho 側）")
calc("rs_rev", "レストラン売上", "円", Y, lambda c: f"{I('rs_days',c)}*{I('rs_covers',c)}*{I('rs_check',c)}", "days × covers × check")
calc("rs_cmr", "限界利益率（25% 支払い後）", "%", P, lambda c: f"1-{I('rs_food',c)}-{I('rs_pay',c)}-{I('rs_share',c)}", "1 − 原価率 − 決済 − 25%", bold=True)
calc("rs_cmr0", "限界利益率（25% がなかった場合）", "%", P, lambda c: f"1-{I('rs_food',c)}-{I('rs_pay',c)}", "比較用")
calc("rs_fc", "レストラン固定費", "円", Y, lambda c: f"{I('rs_labor',c)}+{I('rs_fixed',c)}", "")
calc("rs_be", "損益分岐 売上（25% 支払いあり）", "円", Y, lambda c: f'IF({K("rs_cmr",c)}<=0,"売るほど赤字",{K("rs_fc",c)}/{K("rs_cmr",c)})', "固定費 ÷ 限界利益率", bold=True, safe=True)
calc("rs_be0", "損益分岐 売上（25% なしの場合）", "円", Y, lambda c: f"{K('rs_fc',c)}/{K('rs_cmr0',c)}", "", safe=True)
calc("rs_be_mult", "25% による損益分岐売上の倍率", "倍", "0.00", lambda c: f"{K('rs_be',c)}/{K('rs_be0',c)}", "(1−f−p) ÷ (1−f−p−25%)", safe=True)
calc("rs_be_cov", "損益分岐 客数/日（25% あり）", "人/日", "#,##0", lambda c: f"{K('rs_be',c)}/{I('rs_days',c)}/{I('rs_check',c)}", "", safe=True)
calc("rs_pay_john", "John への支払い（レストラン売上分）", "円", Y, lambda c: f"{K('rs_rev',c)}*{I('rs_share',c)}", "")
calc("rs_pl", "レストラン損益（25% 支払い後）", "円", Y, lambda c: f"{K('rs_rev',c)}*{K('rs_cmr',c)}-{K('rs_fc',c)}", "", bold=True)

sec("⑥ 取り分（Sho / 支配人 / John）— 定義はスイッチ次第")
calc("x_st_rev_side", "Sho 側に入るスタンド＋イベントの売上", "円", Y,
     lambda c: f"IF({I('sw_stand',c)}=2,{K('st_rev',c)},0)+IF({I('sw_event',c)}=2,({K('entry_rev',c)}+{I('att',c)}*{I('d_buy',c)}*{I('d_spend',c)}+N(CHOOSE({I('model',c)},0,{K('fee_B',c)},{K('fee_C',c)})))*{I('weeks',c)},0)", "25% の対象になりうる売上", safe=True)
calc("x_pay_john_extra", "その売上に対する John への支払い", "円", Y, lambda c: f"N({K('x_st_rev_side',c)})*{I('rs_share',c)}*{I('sw_rs_base',c)}", "")
calc("side_pl", "Sho 側の利益（レストラン＋Sho 側区分）", "円", Y,
     lambda c: f"{K('rs_pl',c)}+IF({I('sw_stand',c)}=2,{K('st_pl',c)},0)+IF({I('sw_event',c)}=2,{K('ev_pl_season',c)},0)-{K('x_pay_john_extra',c)}", "", bold=True)
calc("np", "ホテル純利益 NP（分配の元）", "円", Y,
     lambda c: (f"{K('pl_room',c)}+{K('add_pl',c)}+IF({I('sw_event',c)}=1,{K('ev_pl_season',c)},0)+IF({I('sw_stand',c)}=1,{K('st_pl',c)},0)"
                f"+IF({I('sw_rs_to',c)}=2,{K('rs_pay_john',c)}+{K('x_pay_john_extra',c)},0)-{I('mgr_salary',c)}*{I('sw_salary',c)}"),
     "宿泊 + 追加宿泊 + (区分1の)イベント・スタンド + (行き先2なら)25% − (sw_salary=1なら)支配人給与", bold=True)
calc("np_dist", "分配する額（赤字時の扱いを反映）", "円", Y, lambda c: f"IF({K('np',c)}>=0,{K('np',c)},{K('np',c)}*{I('sw_loss',c)})", "")
calc("take_sho", "Sho の取り分（夏季）", "円", Y, lambda c: f"{K('np_dist',c)}*{I('p_sho',c)}+{K('side_pl',c)}*{I('p_side_sho',c)}", "NP×20% + Sho 側利益×本人分", bold=True)
calc("take_side_other", "Sho 側の他の人（いれば）", "円", Y, lambda c: f"{K('side_pl',c)}*(1-{I('p_side_sho',c)})", "D4")
calc("take_mgr", "Yukari の取り分（夏の給与＋NP×20%）", "円", Y, lambda c: f"{I('mgr_salary',c)}+{K('np_dist',c)}*{I('p_mgr',c)}", "給与は sw_salary に関係なく支配人に入る", bold=True)
calc("take_own", "John の取り分（夏季）", "円", Y,
     lambda c: f"IF({K('np',c)}>=0,{K('np',c)}*{I('p_own',c)},{K('np',c)}-{K('np_dist',c)}*({I('p_sho',c)}+{I('p_mgr',c)}))+IF({I('sw_rs_to',c)}=1,{K('rs_pay_john',c)}+{K('x_pay_john_extra',c)},0)-IF({I('sw_salary',c)}=0,{I('mgr_salary',c)},0)",
     "NP×60%（赤字時は残り全部）+ 25%（個人宛なら）− (sw_salary=0 なら)支配人給与", bold=True)
calc("take_check", "検算（取り分合計 − 全体の利益）", "円", Y,
     lambda c: f"{K('take_sho',c)}+{K('take_side_other',c)}+{K('take_mgr',c)}+{K('take_own',c)}-({K('tot_all',c)}+{K('rs_pl',c)}+{K('rs_pay_john',c)})",
     "0 なら漏れなし（p_sho+p_mgr+p_own=100% のとき）")
calc("p_sum", "NP の分配率の合計", "%", P, lambda c: f"{I('p_sho',c)}+{I('p_mgr',c)}+{I('p_own',c)}", "100% でなければ入力ミス")


cs.column_dimensions["A"].width = 13
cs.column_dimensions["B"].width = 52
cs.column_dimensions["C"].width = 8
for col in SC:
    cs.column_dimensions[col].width = 15
cs.column_dimensions["G"].width = 50
cs.freeze_panes = "D5"
for ws_ in (ws, cs):
    for col, name in zip(SC, ["保守", "基本", "強気"]):
        pass

# ---------- Sho への確認事項 ----------
qs = wb.create_sheet("Shoへの確認")
qs["A1"] = "入力に必要な情報（Sho／オーナーに確認）"; qs["A1"].font = Font(bold=True, size=13)
rows = [
    ("Q1", "夏の営業期間（開始日・終了日）、販売可能客室数、夏の料金の考え方、食事提供の有無", "days, rooms, adr, anc"),
    ("Q3", "予算（告知・イベント・人件費）と、オーナーの目標（売上・稼働率・来場者数）", "fc_promo, ev_init, ev_promo_s, 目標"),
    ("Q4", "駐車場の台数・道路の開通時期（来場者数の上限になる）", "att の上限"),
    ("Q5", "キッチンカーの当ての台数、出店料の考え（無料／定額／歩合）、電源・水・トイレの有無", "trucks, fee_flat, fee_pct, equip, misc_ev"),
    ("Q7", "夏は毎年休館（2026-11-18 Sho）→ 夏の実績なし。冬の実績（人数・予約経路・OTA 手数料率）と、稼働率は競合調査 T07 から置く", "ppr, ota_share, ota_fee（occ は T07 から）"),
    ("Q8", "夏の人員（残る人・新規採用・時給）、清掃の委託条件", "fc_staff, wage, staff_n, v_room, fc_clean"),
    ("追加", "夏季の光熱費・保険・システム費の過去の請求額（なければ冬の請求書から按分の方針）", "fc_util, fc_ins, fc_sys"),
    ("追加", "開館にかかる一時費用（点検・水道開栓・修繕）。冬から通年営業なら 0", "fc_open"),
    ("追加", "減価償却・リース・借入返済を夏季の固定費に含めるか（含めると結論が変わりうる）", "fc_other"),
    ("追加", "酒類をイベントで売るか（許可は T05 Law）、物販の内容と原価", "d_buy, d_spend, d_margin"),
    ("追加", "イベントの曜日と時間（前泊・当泊が見込めるか）", "ev_nights, conv"),
    ("⑤", "かき氷機の正式な見積（機種・本体価格・月額・契約期間・中途解約の可否・保守）。『約100万円クラスを月2万円台』は Sho の伝聞で未確認", "ks_rent, st_months"),
    ("⑤", "山頂スタンドの場所（土地の所有者・国立公園の区域か）、電源・水・氷と機材の運搬手段", "st_daily, st_init（許可は T05 Law）"),
    ("⑤", "ホテルが持つ飲食店営業許可の内容と、山頂の売り場で別の許可が要るか（保健所に確認）", "st_init・実施の可否"),
    ("⑤", "かき氷・コーヒーの価格、Sho 自身の時間を費用に入れるか", "ks_price, cf_price, st_wage"),
    ("D1", "NP の定義: 何を差し引いた後か（減価償却・借入返済・オーナーの他ホテルとの共通費・固定資産税・本部費）。赤字のときは誰が負担するか", "fc_*, sw_loss"),
    ("D2", "Yukari の夏の給与は NP を出す前の費用か（NP から引くか）、オーナーが別に払うか。夏の給与額と期間", "mgr_salary, sw_salary"),
    ("D3", "レストランは 20/20/60 の外か。25% は John 個人に払うのか、ホテルの売上（NP の中）に入るのか。25% の対象は税抜売上か税込か、宿泊者の朝夕食も含むか", "sw_rs_to, rs_share"),
    ("D4", "Sho 側のレストラン利益の分け方（Sho 単独か、支配人や他の人と分けるか）。ComInc. の事業として計上するか", "p_side_sho"),
    ("D5", "かき氷・コーヒーとキッチンカーの出店料・ドリンク物販は、ホテル NP 側か Sho 側か。Sho 側なら 25% の対象か", "sw_stand, sw_event, sw_rs_base"),
    ("D6", "宿泊の食事（付帯売上）はレストラン側に入るか。入るなら宿泊の anc は 0 にする（二重計上を防ぐ）", "anc, anc_m"),
    ("D7", "光熱費・清掃・人件費のうちレストランが負担する按分ルール", "rs_fixed, fc_util"),
    ("D8", "20/20/60 と 25% は夏季のみ（Sho 2026-11-18）。口頭か契約書か、夏季の始まりと終わりの日付（冬の別契約との境目）", "全体"),
]
for i, h in enumerate(["#", "確認すること", "埋まる入力"]):
    c = qs.cell(row=3, column=i + 1, value=h); c.font = BOLD; c.fill = HEAD_FILL
for i, rr in enumerate(rows):
    for j, v in enumerate(rr):
        qs.cell(row=4 + i, column=j + 1, value=v)
qs.column_dimensions["A"].width = 7
qs.column_dimensions["B"].width = 90
qs.column_dimensions["C"].width = 40

wb.calculation.fullCalcOnLoad = True
wb.save(OUT)
print("saved", OUT, "sample" if SAMPLE else "blank")
