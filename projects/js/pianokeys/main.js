// 🎹 Piano key setup
const keys = document.querySelectorAll('.key');
const notes = [];

keys.forEach(key => {
  notes.push(key);
});

// 🎨 Step 1 & 2: Functions for changing background
function keyPlay(event) {
  event.target.style.backgroundColor = '#fbc531';
}

function keyReturn(event) {
  event.target.style.backgroundColor = '';
}

// 🎼 Step 3–5: Assign events to notes
function assignKeyEvents(note) {
  note.onmousedown = keyPlay;
  note.onmouseup = keyReturn;
}

// 🎹 Step 6: Loop through notes and assign handlers
notes.forEach(assignKeyEvents);

// 🎵 Step 8: Progress buttons
const nextOne = document.getElementById('next-one');
const nextTwo = document.getElementById('next-two');
const nextThree = document.getElementById('next-three');
const startOver = document.getElementById('start-over');

// 🎤 Lyrics
const wordOne = document.getElementById('word-one');
const wordTwo = document.getElementById('word-two');
const wordThree = document.getElementById('word-three');
const wordFour = document.getElementById('word-four');
const wordFive = document.getElementById('word-five');
const wordSix = document.getElementById('word-six');
const lastLyric = document.getElementById('lastLyric');

// 🎶 Notes
const letterNoteOne = document.getElementById('letter-note-one');
const letterNoteTwo = document.getElementById('letter-note-two');
const letterNoteThree = document.getElementById('letter-note-three');
const letterNoteFour = document.getElementById('letter-note-four');
const letterNoteFive = document.getElementById('letter-note-five');
const letterNoteSix = document.getElementById('letter-note-six');

// 👇 Step 9–10: Click event on nextOne
nextOne.onclick = function () {
  nextTwo.hidden = false;
  nextOne.hidden = true;

  letterNoteFive.textContent = 'D';
  letterNoteSix.textContent = 'C';
};

// 👉 Step 11–15: Click event on nextTwo
nextTwo.onclick = function () {
  nextThree.hidden = false;
  nextTwo.hidden = true;

  wordFive.textContent = 'DEAR';
  wordSix.textContent = 'FRI-';
  lastLyric.style.display = 'inline-block';

  letterNoteThree.textContent = 'G';
  letterNoteFour.textContent = 'E';
  letterNoteFive.textContent = 'C';
  letterNoteSix.textContent = 'B';
};

// 🎯 Step 16–20: Click event on nextThree
nextThree.onclick = function () {
  startOver.hidden = false;
  nextThree.hidden = true;

  wordOne.textContent = 'HAP-';
  wordTwo.textContent = 'PY';
  wordThree.textContent = 'BIRTH';
  wordFour.textContent = 'DAY';
  wordFive.textContent = 'TO';
  wordSix.textContent = 'YOU!';

  letterNoteOne.textContent = 'F';
  letterNoteTwo.textContent = 'F';
  letterNoteThree.textContent = 'E';
  letterNoteFour.textContent = 'C';
  letterNoteFive.textContent = 'D';
  letterNoteSix.textContent = 'C';

  lastLyric.style.display = 'none';
};
