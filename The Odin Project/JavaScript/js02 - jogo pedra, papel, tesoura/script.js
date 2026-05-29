function getComputerChoice(){
    let computerChoice = ['pedra', 'papel', 'tesoura']
    let choice = Math.floor(Math.random() * 3)
    return computerChoice[choice]
}

function getHumanChoice(){
    let humanChoice = prompt(`Escolha entre pedra, papel ou tesoura: `)
    return humanChoice.toLowerCase()
}

function playRound(humanChoice, computerChoice){
    console.log(`Você escolheu ${humanChoice} e o computador escolheu ${computerChoice}`)
    if (humanChoice === computerChoice){
        console.log(`Empate. Tente novamente!`)
        return 0
    } else if (humanChoice === 'pedra' && computerChoice === 'papel' 
                || humanChoice === 'papel' && computerChoice === 'tesoura'
                || humanChoice === 'tesoura' && computerChoice === 'pedra'){
        console.log(`Você perdeu`)
        return 1
    } else {
        console.log(`Você ganhou!!!`)
        return 2
    }
}

function playGame(){
    humanScore = 0
    computerScore = 0
    for (i = 1; i <= 5; i++){
        computerResult = getComputerChoice()
        humanResult = getHumanChoice()
        result = playRound(humanResult, computerResult)

        if (result === 1){
            computerScore += 1
        } else if (result === 2){
            humanScore += 1
        }
        
        console.log(`Placar: Você ${humanScore} pontos | Computador ${computerScore} pontos`)
    }
     if (humanScore > computerScore){
        console.log(`Você venceu o computador!!`)
    } else {
        console.log(`A máquina venceu você. Tente novamente.`)
    }
}

playGame()