import streamlit as st
import streamlit.components.v1 as components


# page conf
st.set_page_config(
    page_title="Flying Words",
    layout="centered")
st.title('Radio Player')

HTML = """

<style>
html,
body {
    height: 100%;
}

body {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    color: black;
}

audio {
    margin-bottom: 24px;
}

video {
    max-width: 80%;
}

</style>


<audio class="player" src="/home/david/code/D-Srdln/deaf_radio/13917-09.06.2022-ITEMA_23053434-2022C22191S0160-21.mp3" controls></audio>

<div class="lyrics" src="/home/david/code/D-Srdln/deaf_radio/result_test.txt" style="display: none">

</div>


<script language="javascript">

const player = document.querySelector('.player')
const lyrics = document.querySelector('.lyrics')
const lines = lyrics.textContent.trim().split('\\n')

lyrics.removeAttribute('style')
lyrics.innerText = ''

let syncData = []

lines.map((line, index) => {
    const [time, text] = line.trim().split('|')
    syncData.push({'start': time.trim(), 'text': text.trim()})
})

player.addEventListener('timeupdate', () => {
    lyrics.innerText = ''
    syncData.forEach((item) => {
        if (player.currentTime >= item.start)
        {
            console.log(lyrics.innerText)
            lyrics.innerText += ' ' + item.text
        }
    })
})

</script>

"""

components.html(HTML)
