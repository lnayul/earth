<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>그린 디펜더: 2050 기후 시뮬레이션</title>
    <style>
        :root {
            --primary-color: #2e7d32;
            --secondary-color: #81c784;
            --danger-color: #d32f2f;
            --warning-color: #f57c00;
            --bg-color: #f1f8e9;
            --card-bg: #ffffff;
            --text-color: #333333;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        body {
            background-color: var(--bg-color);
            color: var(--text-color);
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            padding: 20px;
        }

        .game-container {
            width: 100%;
            max-width: 600px;
            background-color: var(--card-bg);
            border-radius: 16px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.1);
            overflow: hidden;
            display: flex;
            flex-direction: column;
        }

        header {
            background: linear-gradient(135deg, #2e7d32, #1b5e20);
            color: white;
            padding: 20px;
            text-align: center;
        }

        header h1 {
            font-size: 1.5rem;
            margin-bottom: 5px;
        }

        header p {
            font-size: 0.9rem;
            opacity: 0.9;
        }

        .status-panel {
            padding: 15px 20px;
            background-color: #f9fbe7;
            border-bottom: 1px solid #e0e0e0;
            display: flex;
            flex-direction: column;
            gap: 10px;
        }

        .status-row {
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-weight: bold;
            font-size: 0.95rem;
        }

        .hp-bar-container {
            width: 100%;
            height: 20px;
            background-color: #e0e0e0;
            border-radius: 10px;
            overflow: hidden;
            position: relative;
        }

        .hp-bar {
            height: 100%;
            width: 100%;
            background-color: var(--primary-color);
            transition: width 0.5s ease, background-color 0.5s ease;
        }

        .stats-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 10px;
            font-size: 0.9rem;
        }

        .stat-item {
            background: white;
            padding: 6px 12px;
            border-radius: 8px;
            border: 1px solid #c8e6c9;
            display: flex;
            justify-content: space-between;
        }

        .content-area {
            padding: 25px;
            display: flex;
            flex-direction: column;
            gap: 20px;
        }

        .year-indicator {
            font-size: 1.1rem;
            font-weight: bold;
            color: var(--primary-color);
            text-align: center;
        }

        .scenario-box {
            background-color: #f4f9f4;
            border-left: 5px solid var(--primary-color);
            padding: 15px;
            border-radius: 0 8px 8px 0;
            font-size: 1rem;
            line-height: 1.5;
            min-height: 80px;
        }

        .choices-container {
            display: flex;
            flex-direction: column;
            gap: 12px;
        }

        .choice-btn {
            background-color: white;
            border: 2px solid #c8e6c9;
            padding: 15px;
            border-radius: 10px;
            cursor: pointer;
            text-align: left;
            font-size: 0.95rem;
            transition: all 0.2s ease;
            box-shadow: 0 2px 5px rgba(0,0,0,0.02);
        }

        .choice-btn:hover:not(:disabled) {
            background-color: #e8f5e9;
            border-color: var(--primary-color);
            transform: translateY(-2px);
        }

        .choice-btn:active:not(:disabled) {
            transform: translateY(0);
        }

        .feedback-box {
            margin-top: 10px;
            padding: 12px;
            border-radius: 8px;
            background-color: #e3f2fd;
            color: #0d47a1;
            font-size: 0.9rem;
            line-height: 1.4;
            display: none;
        }

        .next-btn {
            background-color: var(--primary-color);
            color: white;
            border: none;
            padding: 12px;
            border-radius: 8px;
            font-weight: bold;
            cursor: pointer;
            font-size: 1rem;
            transition: background-color 0.2s;
            display: none;
        }

        .next-btn:hover {
            background-color: #1b5e20;
        }

        .screen {
            display: none;
        }

        .screen.active {
            display: flex;
            flex-direction: column;
            gap: 20px;
        }

        .intro-screen, .ending-screen {
            text-align: center;
            padding: 30px;
            gap: 20px;
        }

        .intro-screen h2, .ending-screen h2 {
            font-size: 1.6rem;
            color: var(--primary-color);
        }

        .intro-screen p, .ending-screen p {
            line-height: 1.6;
            color: #555;
        }

        .start-btn {
            background-color: var(--primary-color);
            color: white;
            border: none;
            padding: 15px 30px;
            border-radius: 30px;
            font-size: 1.1rem;
            font-weight: bold;
            cursor: pointer;
            box-shadow: 0 4px 10px rgba(46, 125, 50, 0.3);
            transition: transform 0.2s;
        }

        .start-btn:hover {
            transform: scale(1.05);
        }

        .earth-visual {
            font-size: 3rem;
            text-align: center;
            margin-bottom: -10px;
        }
    </style>
</head>
<body>

<div class="game-container">
    <header>
        <h1>🌍 그린 디펜더: 2050</h1>
        <p>기후 변화 대응 정책 시뮬레이션 게임</p>
    </header>

    <!-- 시작 화면 -->
    <div id="introScreen" class="screen active intro-screen">
        <div class="earth-visual">🌱</div>
        <h2>지구를 구하기 위한 당신의 선택</h2>
        <p>
            환영합니다! 당신은 국제 기후 대책 위원회의 최고 의사결정자입니다.<br>
            매년 쏟아지는 기후 위기 상황 속에서 최선의 정책을 선택하여<br>
            <strong>2050년까지 지구 체력(HP)을 유지</strong>하고 지구를 구해주세요!
        </p>
        <button class="start-btn" onclick="startGame()">게임 시작하기</button>
    </div>

    <!-- 게임 플레이 화면 -->
    <div id="gameScreen" class="screen">
        <div class="status-panel">
            <div class="status-row">
                <span>지구 체력 (HP)</span>
                <span id="hpText">100 / 100</span>
            </div>
            <div class="hp-bar-container">
                <div id="hpBar" class="hp-bar"></div>
            </div>
            <div class="stats-grid">
                <div class="stat-item">
                    <span>탄소 농도:</span>
                    <span id="carbonText">410 ppm</span>
                </div>
                <div class="stat-item">
                    <span>잔여 예산:</span>
                    <span id="budgetText">100 억$</span>
                </div>
            </div>
        </div>

        <div class="content-area">
            <div id="yearIndicator" class="year-indicator">📅 2024년</div>
            <div id="scenarioBox" class="scenario-box">
                시나리오가 여기에 표시됩니다.
            </div>

            <div id="choicesContainer" class="choices-container">
                <!-- 선택지 버튼들이 동적으로 생성됩니다 -->
            </div>

            <div id="feedbackBox" class="feedback-box">
                피드백 내용이 여기에 표시됩니다.
            </div>

            <button id="nextBtn" class="next-btn" onclick="nextTurn()">다음 해로 진행하기</button>
        </div>
    </div>

    <!-- 엔딩 화면 -->
    <div id="endingScreen" class="screen ending-screen">
        <div id="endingVisual" class="earth-visual">🏆</div>
        <h2 id="endingTitle">엔딩 제목</h2>
        <p id="endingDesc">엔딩 설명이 여기에 표시됩니다.</p>
        <button class="start-btn" onclick="resetGame()">다시 도전하기</button>
    </div>
</div>

<script>
    // 게임 데이터 및 시나리오 정의
    const scenarios = [
        {
            year: 2024,
            text: "첫해부터 폭염과 가뭄이 전 세계를 강타했습니다. 화력발전소 비중을 줄이고 재생에너지 투자를 대폭 늘려야 한다는 목소리가 높습니다.",
            choices: [
                {
                    text: "A안: 대규모 재생에너지 보조금 지급 및 화력발전 조기 폐쇄 추진",
                    hpChange: 0,
                    carbonChange: -15,
                    budgetChange: -30,
                    feedback: "탁월한 선택입니다! 탄소 배출이 크게 줄었지만, 초기 예산 소모가 컸습니다."
                },
                {
                    text: "B안: 경제 성장을 위해 화력발전을 유지하되, 효율성 개선 장치만 도입",
                    hpChange: -15,
                    carbonChange: +10,
                    budgetChange: -10,
                    feedback: "경제적 타격은 줄었으나, 탄소 배출이 늘어나며 지구 온도가 치솟았습니다."
                }
            ]
        },
        {
            year: 2028,
            text: "내연기관 자동차로 인한 도심 대기오염이 심각해졌습니다. 강력한 교통 규제 카드를 꺼내들 시점입니다.",
            choices: [
                {
                    text: "A안: 2035년까지 내연기관 차량 판매 전면 금지 및 전기차 보급 가속화",
                    hpChange: +5,
                    carbonChange: -20,
                    budgetChange: -25,
                    feedback: "친환경 교통 체계로의 전환에 성공했습니다. 공기가 한층 맑아졌습니다."
                },
                {
                    text: "B안: 자동차 업계 반발을 고려해 친환경차 세제 혜택만 자율적으로 운영",
                    hpChange: -10,
                    carbonChange: +5,
                    budgetChange: -5,
                    feedback: "변화의 속도가 너무 느립니다. 대기오염과 탄소 수치가 여전히 높습니다."
                }
            ]
        },
        {
            year: 2033,
            text: "지구 온난화로 북극 빙하가 빠르게 녹아내리며 해수면 상승 위기가 고조되고 있습니다. 대규모 해안 방재 대책이 필요합니다.",
            choices: [
                {
                    text: "A안: 대대적인 해안 방벽 건설 및 저지대 주민 대피 계획 수립",
                    hpChange: -5,
                    carbonChange: 0,
                    budgetChange: -35,
                    feedback: "막대한 예산이 들었지만 해수면 상승으로부터 시민들의 안전을 지켰습니다."
                },
                {
                    text: "B안: 방재 예산을 아껴 근본적인 해양 생태계 복원 및 탄소 흡수원(숲/갯벌) 확충에 투자",
                    hpChange: +10,
                    carbonChange: -25,
                    budgetChange: -20,
                    feedback: "자연의 자정 능력을 높여 탄소 흡수가 늘어났습니다. 장기적으로 매우 현명한 선택입니다!"
                }
            ]
        },
        {
            year: 2038,
            text: "산업계 전반에서 탄소세 도입에 대한 반발이 거셉니다. 하지만 기후 위기는 임계점을 향해가고 있습니다.",
            choices: [
                {
                    text: "A안: 강력한 탄소 국경세 및 고탄소 배출 기업에 무거운 벌칙 부과",
                    hpChange: +5,
                    carbonChange: -20,
                    budgetChange: +15, // 벌금 수입
                    feedback: "기업들이 마침내 친환경 공정으로 대거 전환하기 시작했습니다. 탄소 수치가 안정화됩니다."
                },
                {
                    text: "B안: 기업의 자발적 감축에 맡기고 규제를 최소화하여 경제 안정 도모",
                    hpChange: -20,
                    carbonChange: +15,
                    budgetChange: 0,
                    feedback: "기업들은 눈앞의 이익을 쫓았고, 지구는 통제 불능의 온난화 궤도에 접어듭니다."
                }
            ]
        },
        {
            year: 2044,
            text: "전 세계적인 식량 위기와 생물다양성 파괴 경보가 울렸습니다. 마지막 분수령이 될 대책을 선택하세요.",
            choices: [
                {
                    text: "A안: 전 지구적 식량 안보 연대 결성 및 농업 부문 탄소 배출 감축 기술 전면 지원",
                    hpChange: +10,
                    carbonChange: -15,
                    budgetChange: -25,
                    feedback: "농업 혁신을 통해 식량 위기를 극복하고 생태계를 보호하는 데 성공했습니다."
                },
                {
                    text: "B안: 기존 농업 방식을 유지하며 개별 국가의 자율 해결 유도",
                    hpChange: -20,
                    carbonChange: +10,
                    budgetChange: -5,
                    feedback: "기후 재앙으로 인한 식량 생산량 급감으로 지구 생태계가 큰 타격을 입었습니다."
                }
            ]
        },
        {
            year: 2049,
            text: "2050년의 문턱입니다. 마지막으로 남은 예산을 지구의 미래에 모두 쏟아부어야 합니다.",
            choices: [
                {
                    text: "A안: 전 지구적 탄소 포집 기술(CCUS) 대규모 상용화 및 숲 복원 프로젝트 완료",
                    hpChange: +15,
                    carbonChange: -30,
                    budgetChange: -30,
                    feedback: "대기 중의 남은 탄소까지 깔끔하게 정화하며 마침내 지속 가능한 지구를 만들었습니다!"
                },
                {
                    text: "B안: 현재 상태 유지 및 기후 적응 체계 유지",
                    hpChange: -15,
                    carbonChange: 0,
                    budgetChange: 0,
                    feedback: "변화를 멈춘 사이에 기후 불안정성이 최고조에 달했습니다."
                }
            ]
        }
    ];

    let currentTurn = 0;
    let gameState = {
        hp: 100,
        carbon: 410,
        budget: 100
    };

    // DOM 요소들
    const introScreen = document.getElementById('introScreen');
    const gameScreen = document.getElementById('gameScreen');
    const endingScreen = document.getElementById('endingScreen');
    
    const hpText = document.getElementById('hpText');
    const hpBar = document.getElementById('hpBar');
    const carbonText = document.getElementById('carbonText');
    const budgetText = document.getElementById('budgetText');
    const yearIndicator = document.getElementById('yearIndicator');
    const scenarioBox = document.getElementById('scenarioBox');
    const choicesContainer = document.getElementById('choicesContainer');
    const feedbackBox = document.getElementById('feedbackBox');
    const nextBtn = document.getElementById('nextBtn');

    function startGame() {
        currentTurn = 0;
        gameState = {
            hp: 100,
            carbon: 410,
            budget: 100
        };
        introScreen.classList.remove('active');
        endingScreen.classList.remove('active');
        gameScreen.classList.add('active');
        updateUI();
        loadScenario();
    }

    function updateUI() {
        hpText.textContent = `${gameState.hp} / 100`;
        hpBar.style.width = `${Math.max(0, Math.min(100, gameState.hp))}%`;
        
        // HP 바 색상 동적 변경
        if (gameState.hp > 60) {
            hpBar.style.backgroundColor = 'var(--primary-color)';
        } else if (gameState.hp > 30) {
            hpBar.style.backgroundColor = 'var(--warning-color)';
        } else {
            hpBar.style.backgroundColor = 'var(--danger-color)';
        }

        carbonText.textContent = `${gameState.carbon} ppm`;
        budgetText.textContent = `${gameState.budget} 억$`;
    }

    function loadScenario() {
        if (currentTurn >= scenarios.length || gameState.hp <= 0) {
            endGame();
            return;
        }

        const scenario = scenarios[currentTurn];
        yearIndicator.textContent = `📅 ${scenario.year}년`;
        scenarioBox.textContent = scenario.text;
        feedbackBox.style.display = 'none';
        nextBtn.style.display = 'none';

        choicesContainer.innerHTML = '';
        scenario.choices.forEach((choice, index) => {
            const btn = document.createElement('button');
            btn.className = 'choice-btn';
            btn.textContent = choice.text;
            btn.onclick = () => selectChoice(index);
            choicesContainer.appendChild(btn);
        });
    }

    function selectChoice(choiceIndex) {
        const scenario = scenarios[currentTurn];
        const choice = scenario.choices[choiceIndex];

        // 수치 반영
        gameState.hp = Math.max(0, Math.min(100, gameState.hp + choice.hpChange));
        gameState.carbon += choice.carbonChange;
        gameState.budget = Math.max(0, gameState.budget + choice.budgetChange);

        updateUI();

        // 선택지 비활성화 및 선택 효과
        const buttons = choicesContainer.getElementsByClassName('choice-btn');
        for (let btn of buttons) {
            btn.disabled = true;
            btn.style.opacity = '0.6';
        }
        buttons[choiceIndex].style.opacity = '1';
        buttons[choiceIndex].style.borderColor = 'var(--primary-color)';
        buttons[choiceIndex].style.backgroundColor = '#e8f5e9';

        // 피드백 표시
        feedbackBox.textContent = choice.feedback;
        feedbackBox.style.display = 'block';

        // HP가 0이 되면 즉시 게임 종료
        if (gameState.hp <= 0) {
            setTimeout(endGame, 1500);
            return;
        }

        nextBtn.style.display = 'block';
    }

    function nextTurn() {
        currentTurn++;
        loadScenario();
    }

    function endGame() {
        gameScreen.classList.remove('active');
        endingScreen.classList.add('active');

        const endingVisual = document.getElementById('endingVisual');
        const endingTitle = document.getElementById('endingTitle');
        const endingDesc = document.getElementById('endingDesc');

        if (gameState.hp > 0 && currentTurn >= scenarios.length) {
            endingVisual.textContent = '🌟';
            endingTitle.textContent = '지구 구출 성공! (2050 지속가능성 달성)';
            endingDesc.innerHTML = `축하합니다! 당신의 현명한 정책 선택 덕분에 지구는 최악의 기후 위기를 이겨내고 2050년에 도달했습니다.<br>탄소 수치: <strong>${gameState.carbon} ppm</strong>, 잔여 HP: <strong>${gameState.hp}</strong><br>미래 세대에게 건강한 지구를 물려주었습니다!`;
        } else {
            endingVisual.textContent = '🚨';
            endingTitle.textContent = '지구 위기 발생! (게임 오버)';
            endingDesc.innerHTML = `기후 재앙을 막지 못해 지구 체력이 바닥났습니다.<br>지구의 탄소 농도가 임계점을 초과하여 생태계가 붕괴되었습니다.<br>지속 가능한 미래를 위한 과감하고 올바른 선택의 중요성을 다시 한번 깨닫게 됩니다.`;
        }
    }
</script>

</body>
</html>
