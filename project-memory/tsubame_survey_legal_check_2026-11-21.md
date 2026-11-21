# 燕ハイランドホテル 冬季アンケート（Jotform）法令チェック — 下書き
作成: 2026-11-21 / Law。扱い: ホテルの案件。次: Cat（文言）→ Hana（事実）。読んだ: CLAUDE.md、playbook/README.md・law.md、tsubame_summer_legal_2026-11-18.md
出典の限界: 官公庁サイトは原文未読。条文・告示の番号と数値は Law の知識で、**すべて未確認（e-Gov・消費者庁で照合要）**。
1. 景品表示法（2条3項 景品類、告示「景品類等の指定」、総付景品告示〔昭52告示5〕、運用基準〔昭52事務局長通達7〕）
- 🔴 無料ドリンク: 来店・宿泊に付随して渡すので、購入不要でも「取引に附随」する景品類になりうる。購入不要の来店だけなら取引価額は100円扱い→上限200円（未確認）で、¥600〜1,000は超える。ビール等は同種の値引きとも言いにくい
  修正: 「宿泊者限定」にする。上限は宿泊額の20%（1,000円以上の取引。未確認）で、¥39,000なら足りる。来店客向けなら「ご注文合計¥3,500以上でビール、¥5,000以上でかき氷」。店頭の定価で計算する
- 🟢 直販10%引き: 値引きで景品規制の外。🟡 ただし¥39,000の実績がまだない。「通常料金」と書くなら、実際にその料金で売る（二重価格ガイドライン、景表法5条2号）。「最安」は書かない
- 🟢 友達紹介: 紹介者に上乗せ特典がなく、登録者全員が同じ特典なので別枠の景品にならない。紹介者への追加特典を付けたら再確認
- 🟡 営業が予定・未確定なので「2027年に営業する場合に有効」と明記（不当表示・契約責任の予防）。特典の費用を誰が持つか（Sho のテナント売上25%の計算）は契約で決める
2. 特定電子メール法・個人情報保護法
- 🔴 同意文: 事業者が特定されていない。特定電子メール法3条（同意なき広告メール禁止）、5条（名称・住所・配信停止の連絡先の表示）。同意はチェックボックス（初期は未チェック）で、同意日時をJotformに残す（4条、保存期間は未確認）
- 🔴「運営するホテル」: 個人情報保護法17条・21条（利用目的の特定・通知公表）のため、**取扱事業者は法人名または屋号で書く**（燕ハイランドホテルの運営主体の正式名称は未確認 → John に確認）。Sho／ComInc. がJotformを設定・管理するなら委託先になり、委託契約（25条）が要る
- 最低限の記載: 事業者名・住所・問い合わせと配信停止の窓口（メール／電話）、取得項目、利用目的（案内の送信と、企画検討のための統計利用も書く）、第三者提供なし、Jotform（米国サーバー）に保管（28条・23条 外的環境の把握。🟡 データ保管地域・契約は未確認）、開示等の請求窓口
- 🟡 紹介者の氏名: 第三者の個人情報を本人以外が入力する。目的を「特典の確認のみ」と書き、ニックネーム可、使ったら削除する。氏名・メールは任意と明記
- 🟢 EUのゲスト: 日本で宿泊する人の案内はGDPR対象外の可能性が高い（未確認）。同意と配信停止があれば実務上は足りる
3. 飲酒
- 🔴 道路交通法65条2項（運転のおそれがある者への酒類提供の禁止）と、未成年者飲酒禁止法（年齢確認）。罰則の条番号は未確認
  修正: 「20歳未満の方・お車を運転される方にはアルコールを提供できません。ビールは同額のコーヒー等に変更できます」
4. その他
- 🔴 特典を引き換える方法（登録画面の提示か、コード）が未定。メールが任意だと、メールなしの人に特典を渡す手段がない
- 🟡 店の営業許可（飲食店営業・酒類）の名義が Sho かホテルかは未確認 → ホテルに許可証の写しを依頼
## 提案文言（案。Sho／John の決定待ち）
特典JP: 「2027年グリーンシーズンに燕ハイランドホテルへご宿泊の方（ご登録の本人と、お名前を紹介者に入力してご登録のお友達）に、ご宿泊中お1人につきドリンク1杯（ビール、コーヒー、かき氷から1つ）をサービスします。20歳未満の方・お車を運転される方へのアルコールの提供はできません。あわせて、公式サイト・お電話での直接予約に限り、通常の宿泊料金から10%引きとなります。2027年の営業・料金は予定で、営業する場合に有効です。他の割引との併用はできません。」
特典EN: "For stays at Tsubame Highland Hotel in the 2027 green season, you and any friend who registers using your name each get one free drink per person during your stay (beer, coffee or shaved ice). We cannot serve alcohol to anyone under 20 or anyone driving. Direct bookings through our official website or by phone also get 10% off the regular room rate. 2027 operations and rates are planned and apply only if we open; cannot be combined with other discounts."
同意JP: 「☐ [運営主体の正式名称]（燕ハイランドホテル運営、[住所]、[連絡先メール・電話]）から、2027年グリーンシーズンの宿泊・営業の案内（広告メールを含む）をメールで受け取ることに同意します。メールアドレスは案内の送信のみに使用し、同社が管理します（Jotform 米国サーバーに保管）。各メールのリンクまたは上記連絡先から、いつでも配信停止・同意の撤回ができます。個人情報の取扱いは[プライバシーポリシー]をご覧ください。」
同意EN: "☐ I agree to receive emails about 2027 green-season stays and operations (including promotional emails) from [legal name], operator of Tsubame Highland Hotel ([address], [email/phone]). My email is used only for sending these messages and is managed by that company (stored on Jotform servers in the US). I can unsubscribe or withdraw consent at any time via the link in each email or the contact above. See the [Privacy Policy]."
Unconfirmed: 条文・数値すべて（原文照合）／運営主体の正式名称／許可名義／Jotform の保管地域と契約／宿泊料金の税込・税別／特典の引換方法
Conflicts: なし
