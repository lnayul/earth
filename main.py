<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>탄소 순환 시뮬레이터: 우리가 바꾸면 지구가 변한다</title>
    <style>
        :root {
            --bg-color: #0b132b;
            --card-bg: rgba(28, 37, 65, 0.85);
            --primary: #4cc9f0;
            --accent-green: #57cc99;
            --accent-red: #f72585;
            --text-main: #edf2f4;
            --text-sub: #8d99ae;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: 'Pretendard', 'Apple SD Gothic Neo', sans-serif;
        }

        body {
            background-color: var(--bg-color);
            color: var(--text-main);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
            background-image: radial-gradient(circle at 50% 10%, #1c2541 0%, #0b132b 80%);
        }

        .game-container {
            width: 100%;
            max-width: 800px;
            background: var(--card-bg);
            border-radius: 20px;
            padding: 30px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            position: relative;
            overflow: hidden;
        }

        header {
            text-align: center;
            margin-bottom: 25px;
            border-bottom: 1px solid rgba(255, 255, 255, 0.1);
            padding-bottom: 15px;
        }

        header h1 {
            font-size: 1.8rem;
            color: var(--primary);
            margin-bottom: 8px;
            text-shadow: 0 0 10px rgba(76, 201, 240, 0.3);
        }

        header p {
            font-size: 0.95rem;
            color: var(--text-sub);
            line-height: 1.4;
        }

        /* Earth Display & Status */
        .dashboard {
            display: grid;
            grid-template-columns: 1fr 2fr;
            gap: 20px;
            margin-bottom: 25px;
            background: rgba(11, 19, 43, 0.6);
            padding: 20px;
            border-radius: 15px;
        }

        .earth-visual {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
        }

        .earth-icon {
            font-size: 5rem;
            filter: drop-shadow(0 0 15px rgba(87, 204, 153, 0.5));
            transition: all 0.5s ease;
        }

        .year-badge {
            margin-top: 10px;
            background: var(--primary);
            color: #000;
            font-weight: bold;
            padding: 4px 12px;
            border-radius: 12px;
            font-size: 1.1rem;
        }

        .stats-panel {
            display: flex;
            flex-direction: column;
            justify-content: center;
            gap: 12px;
        }

        .stat-group {
            display: flex;
            flex-direction: column;
            gap: 4px;
        }

        .stat-label {
            display: flex;
            justify-content: space-between;
            font-size: 0.85rem;
            color: var(--text-sub);
        }

        .bar-bg {
            width: 100%;
            height: 14px;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 7px;
            overflow: hidden;
            position: relative;
        }

        .bar-fill {
            height: 100%;
            width: 100%;
            border-radius: 7px;
            transition: width 0.5s ease, background-color 0.5s ease;
        }

        #hp-bar { background-color: var(--accent-green); }
        #co2-bar { background-color: var(--primary); }
        #budget-bar { background-color: #f7b801; }

        /* Card / Event Area */
        .event-card {
            background: rgba(255, 255, 255, 0.05);
            border-radius: 15px;
            padding: 20px;
            margin-bottom: 20px;
            border: 1px solid rgba(255, 255, 255, 0.05);
        }

        .event-title {
            font-size: 1.1rem;
            color: #fff;
            margin-bottom: 10px;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .event-desc {
            font-size: 0.95rem;
            line-height: 1.5;
            color: var(--text-main);
            margin-bottom: 15px;
        }

        .quiz-box {
            background: rgba(76, 201, 240, 0.1);
            border-left: 4px solid var(--primary);
            padding: 10px 15px;
            margin-bottom: 15px;
            font-size: 0.9rem;
            border-radius: 0 8px 8px 0;
        }

        /* Choice Buttons */
        .options-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 12px;
        }

        .btn-option {
            background: rgba(255, 255, 255, 0.1);
            border: 1px solid rgba(255, 255, 255, 0.2);
            color: var(--text-main);
            padding: 14px;
            border-radius: 12px;
            cursor: pointer;
            text-align: left;
            transition: all 0.2s ease;
            display: flex;
            flex-direction: column;
            gap: 5px;
        }

        .btn-option:hover {
            background: rgba(76, 201, 240, 0.2);
            border-color: var(--primary);
            transform: translateY(-2px);
        }

        .btn-option .option-title {
            font-weight: bold;
            font-size: 0.95rem;
            color: var(--primary);
        }

        .btn-option .option-desc {
            font-size: 0.8rem;
            color: var(--text-sub);
        }

        /* Ending Screen */
        .ending-screen {
            position: absolute;
            top: 0; left: 0; width: 100%; height: 100%;
            background: rgba(11, 19, 43, 0.95);
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            padding: 30px;
            text-align: center;
            z-index: 10;
            opacity: 0;
            pointer-events: none;
            transition: opacity 0.5s ease;
        }

        .ending-screen.active {
            opacity: 1;
            pointer-events: all;
        }

        .ending-title {
            font-size: 2rem;
            margin-bottom: 15px;
        }

        .ending-desc {
            font-size: 1rem;
            line-height: 1.6;
            margin-bottom: 25px;
            max-width: 600px;
            color: var(--text-sub);
        }

        .btn-restart {
            background: var(--primary);
            color: #000;
            border: none;
            padding: 12px 30px;
            font-size: 1rem;
            font-weight: bold;
            border-radius: 25px;
            cursor: pointer;
            transition: all 0.2s;
        }

        .btn-restart:hover {
            transform: scale(1.05);
            box-shadow: 0 0 15px rgba(76, 201, 240, 0.5);
        }

        @media (max-width: 600px) {
            .dashboard {
                grid-template-columns: 1fr;
            }
            .options-grid {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>

<div class="game-container">
    <header>
        <h1>탄소 순환 시뮬레이터: 우리가 바꾸면 지구가 변한다</h1>
        <p>기후변화는 지구시스템 전체의 문제입니다. 올바른 정책 선택과 퀴즈를 통해 2050년까지 지구를 지켜내세요!</p>
    </header>

    <div class="dashboard">
        <div class="earth-visual">
            <div class="earth-icon" id="earth-emoji">🌍</div>
            <div class="year-badge" id="year-display">2024년</div>
        </div>

        <div class="stats-panel">
            <div class="stat-group">
                <div class="stat-label">
                    <span>지구 건강도 (HP)</span>
                    <span id="hp-val">100 / 100</span>
                </div>
                <div class="bar-bg">
                    <div class="bar-fill" id="hp-bar" style="width: 100%;"></div>
                </div>
            </div>

            <div class="stat-group">
                <div class="stat-label">
                    <span>대기 중 CO₂ 농도</span>
                    <span id="co2-val">420 ppm</span>
                </div>
                <div class="bar-bg">
                    <div class="bar-fill" id="co2-bar" style="width: 42%;"></div>
                </div>
            </div>

            <div class="stat-group">
                <div class="stat-label">
                    <span>글로벌 예산</span>
                    <span id="budget-val">100억 달러</span>
                </div>
                <div class="bar-bg">
                    <div class="bar-fill" id="budget-bar" style="width: 100%;"></div>
                </div>
            </div>
        </div>
    </div>

    <div class="event-card">
        <div class="event-title" id="event-title">🌱 2024년 기후 의제: 에너지 정책 결정</div>
        <div class="event-desc" id="event-desc">세계 에너지 수요가 늘어나고 있습니다. 새로운 전력망 구축을 위한 핵심 정책을 선택하세요.</div>
        <div class="quiz-box" id="quiz-box">
            💡 <b>지구과학 Q:</b> 화석연료 연소 시 발생하는 주요 온실가스는 무엇일까요?
        </div>

        <div class="options-grid">
            <button class="btn-option" onclick="makeChoice(0)">
                <div class="option-title" id="opt0-title">A안: 재생에너지 비중 40% 확대</div>
                <div class="option-desc" id="opt0-desc">예산 20억 소요, CO₂ 억제 효과 큼. (퀴즈 정답 시 HP 회복)</div>
            </button>
            <button class="btn-option" onclick="makeChoice(1)">
                <div class="option-title" id="opt1-title">B안: 석탄 화력발전소 증설</div>
                <div class="option-desc" id="opt1-desc">예산 단 5억 소요, CO₂ 배출량 대폭 증가. (지구 HP 감소)</div>
            </button>
        </div>
    </div>

    <!-- Ending Overlay -->
    <div class="ending-screen" id="ending-screen">
        <div class="ending-title" id="ending-title">지구 구출 성공!</div>
        <div class="ending-desc" id="ending-desc">설명...</div>
        <button class="btn-restart" onclick="restartGame()">시뮬레이션 다시 시작</button>
    </div>
</div>

<script>
    const scenarioData = [
        {
            year: 2024,
            title: "🌱 2024년: 에너지 전환 정책",
            desc: "세계적으로 전력 수요가 크게 늘고 있습니다. 앞으로의 주력 에너지원을 어디에 투자하시겠습니까?",
            quiz: "💡 <b>지구과학 Q:</b> 대기 중 온실효과를 유발하여 지구 기온을 높이는 대표적 기권 탄소 형태는 이산화탄소(CO₂)입니다.",
            options: [
                {
                    title: "A안: 태양광 및 풍력 발전 확대",
                    desc: "비용: 20억 | CO₂ -10 ppm | HP +5",
                    cost: 20, co2Delta: -10, hpDelta: 5,
                    isCorrect: true
                },
                {
                    title: "B안: 석탄 화력발전소 신규 건설",
                    desc: "비용: 5억 | CO₂ +25 ppm | HP -15",
                    cost: 5, co2Delta: 25, hpDelta: -15,
                    isCorrect: false
                }
            ]
        },
        {
            year: 2030,
            title: "🌳 2030년: 산림 생태계 보호",
            desc: "아마존과 주요 열대우림의 개발 압력이 거세지고 있습니다. 탄소 흡수원인 산림을 어떻게 관리하시겠습니까?",
            quiz: "💡 <b>지구과학 Q:</b> 식물권은 광합성을 통해 대기 중 이산화탄소를 흡수하여 유기물 형태로 탄소를 저장합니다.",
            options: [
                {
                    title: "A안: 열대우림 보호구역 지정 및 복원",
                    desc: "비용: 15억 | CO₂ -15 ppm | HP +10",
                    cost: 15, co2Delta: -15, hpDelta: 10,
                    isCorrect: true
                },
                {
                    title: "B안: 무제한 목재 및 농경지 개발 허용",
                    desc: "비용: -10억(수익) | CO₂ +30 ppm | HP -20",
                    cost: -10, co2Delta: 30, hpDelta: -20,
                    isCorrect: false
                }
            ]
        },
        {
            year: 2036,
            title: "🌊 2036년: 해양 산성화 위기",
            desc: "대기 중 CO₂ 증가는 해양 흡수량 증가로 이어져 해양 산성화(pH 감소)를 일으키고 산호초를 파괴합니다.",
            quiz: "💡 <b>지구과학 Q:</b> 대기 중 이산화탄소가 바다에 많이 용해될수록 해수는 산성화(수권 변화)됩니다.",
            options: [
                {
                    title: "A안: 해양 생태계 보호구역 & 탄소 포집 기술(CCUS)",
                    desc: "비용: 25억 | CO₂ -20 ppm | HP +10",
                    cost: 25, co2Delta: -20, hpDelta: 10,
                    isCorrect: true
                },
                {
                    title: "B안: 방치 후 연안 공업단지 추가 개발",
                    desc: "비용: 0억 | CO₂ +20 ppm | HP -15",
                    cost: 0, co2Delta: 20, hpDelta: -15,
                    isCorrect: false
                }
            ]
        },
        {
            year: 2042,
            title: "🧊 2042년: 빙권 융해와 수면 상승",
            desc: "북극 및 그린란드 빙하가 빠르게 녹으며 반사율(알베도)이 감소하고 해수면이 상승하고 있습니다.",
            quiz: "💡 <b>지구과학 Q:</b> 빙권의 얼음이 녹으면 햇빛 반사량이 줄어들어 지구 온난화가 가속화되는 양의 피드백이 발생합니다.",
            options: [
                {
                    title: "A안: 탄소 배출 강력 규제 및 넷제로 이행",
                    desc: "비용: 30억 | CO₂ -25 ppm | HP +15",
                    cost: 30, co2Delta: -25, hpDelta: 15,
                    isCorrect: true
                },
                {
                    title: "B안: 기후 적응 시설(방파제 구축)만 투자",
                    desc: "비용: 15억 | CO₂ +10 ppm | HP -10",
                    cost: 15, co2Delta: 10, hpDelta: -10,
                    isCorrect: false
                }
            ]
        },
        {
            year: 2050,
            title: "🔮 2050년: 지속 가능한 미래 선택",
            desc: "탄소 중립 달성을 위한 마지막 분기점입니다. 사회 전반의 순환 경제 시스템 구축 여부를 결정해야 합니다.",
            quiz: "💡 <b>지구과학 Q:</b> 지구시스템의 탄소 순환은 기권-수권-생물권-직권이 서로 밀접하게 연결되어 작동합니다.",
            options: [
                {
                    title: "A안: 전 지구적 순환 경제 및 친환경 기술 전면 도입",
                    desc: "비용: 20억 | CO₂ -30 ppm | HP +10",
                    cost: 20, co2Delta: -30, hpDelta: 10,
                    isCorrect: true
                },
                {
                    title: "B안: 화석연료 중심의 기존 경제 체제 유지",
                    desc: "비용: 0억 | CO₂ +40 ppm | HP -25",
                    cost: 0, co2Delta: 40, hpDelta: -25,
                    isCorrect: false
                }
            ]
        }
    ];

    let currentStep = 0;
    let hp = 100;
    let co2 = 420; // ppm
    let budget = 100; // 억 달러

    function updateUI() {
        const scenario = scenarioData[currentStep];

        // Header and Year
        document.getElementById('year-display').innerText = `${scenario.year}년`;
        document.getElementById('event-title').innerText = scenario.title;
        document.getElementById('event-desc').innerText = scenario.desc;
        document.getElementById('quiz-box').innerHTML = scenario.quiz;

        // Bars & Stats
        document.getElementById('hp-val').innerText = `${hp} / 100`;
        document.getElementById('hp-bar').style.width = `${Math.max(0, Math.min(100, hp))}%`;

        document.getElementById('co2-val').innerText = `${co2} ppm`;
        // Normalize 350ppm ~ 600ppm for bar width
        let co2Percent = Math.min(100, Math.max(0, ((co2 - 350) / 250) * 100));
        document.getElementById('co2-bar').style.width = `${co2Percent}%`;

        document.getElementById('budget-val').innerText = `${budget}억 달러`;
        document.getElementById('budget-bar').style.width = `${Math.max(0, Math.min(100, budget))}%`;

        // Earth Mood Dynamic Change
        const earthEmoji = document.getElementById('earth-emoji');
        if (hp >= 75) {
            earthEmoji.innerText = "🌍";
            document.getElementById('hp-bar').style.backgroundColor = 'var(--accent-green)';
        } else if (hp >= 40) {
            earthEmoji.innerText = "🌏";
            document.getElementById('hp-bar').style.backgroundColor = '#f7b801';
        } else {
            earthEmoji.innerText = "🔥";
            document.getElementById('hp-bar').style.backgroundColor = 'var(--accent-red)';
        }

        // Options Text
        document.getElementById('opt0-title').innerText = scenario.options[0].title;
        document.getElementById('opt0-desc').innerText = scenario.options[0].desc;
        document.getElementById('opt1-title').innerText = scenario.options[1].title;
        document.getElementById('opt1-desc').innerText = scenario.options[1].desc;
    }

    function makeChoice(optionIndex) {
        const scenario = scenarioData[currentStep];
        const selected = scenario.options[optionIndex];

        // Apply changes
        budget -= selected.cost;
        co2 += selected.co2Delta;
        hp += selected.hpDelta;

        // Clamp values
        if (hp > 100) hp = 100;

        // Check lose condition
        if (hp <= 0) {
            hp = 0;
            showEnding(false);
            return;
        }

        // Advance step
        currentStep++;

        if (currentStep >= scenarioData.length) {
            showEnding(true);
        } else {
            updateUI();
        }
    }

    function showEnding(isSuccess) {
        const screen = document.getElementById('ending-screen');
        const title = document.getElementById('ending-title');
        const desc = document.getElementById('ending-desc');

        screen.classList.add('active');

        if (isSuccess && hp > 0) {
            title.innerText = "🎉 2050년 지구 구출 성공!";
            title.style.color = "var(--accent-green)";
            desc.innerHTML = `<b>최종 지구 건강도: ${hp} HP / CO₂ 농도: ${co2} ppm</b><br><br>` +
                `당신의 현명한 정책 결정으로 지구시스템의 탄소 순환이 균형을 되찾았습니다!<br>` +
                `대기, 해양, 산림, 빙권이 안정을 유지하며 인류는 지속 가능한 미래를 맞이했습니다.`;
        } else {
            title.innerText = "🚨 지구 위기 발생 (경고)";
            title.style.color = "var(--accent-red)";
            desc.innerHTML = `<b>최종 지구 건강도: ${hp} HP / CO₂ 농도: ${co2} ppm</b><br><br>` +
                `탄소 배출 급증과 환경 파괴로 인해 지구 연쇄 시스템이 붕괴되었습니다.<br>` +
                `해양 산성화, 빙하 융해, 극심한 이상기후로 지구가 회복 불능 상태에 빠졌습니다.<br>` +
                `탄소 배출을 줄이고 탄소 흡수원을 회복하기 위한 노력이 다시 필요합니다!`;
        }
    }

    function restartGame() {
        currentStep = 0;
        hp = 100;
        co2 = 420;
        budget = 100;
        document.getElementById('ending-screen').classList.remove('active');
        updateUI();
    }

    // Initialize Game UI
    updateUI();
</script>
</body>
</html>
  
