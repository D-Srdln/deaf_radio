const player = document.querySelector('.player')
const lyrics = document.querySelector('.test')
const lines = lyrics.textContent.trim().split('\n')


lyrics.removeAttribute('style')
lyrics.innerText = ''

let syncData = []

lines.map((line, index) => {
    const [time, text] = line.trim().split('|')
    syncData.push({'start': time.trim(), 'text': text.trim()})
    document.getElementById('line').scrollIntoView();
})

player.addEventListener('timeupdate', () => {
    syncData.forEach((item) => {
        if (player.currentTime >= item.start) lyrics.innerText = item.text
    })
})


//window.scrollBy(0, 100);
//element.scrollIntoView(behavior=smooth);
//document.getElementById('line').scrollIntoView();
