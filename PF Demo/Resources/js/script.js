let coinCount = 0;
let sightWords = true;

phonics  = ["th.m4a", 
            "qu.m4a",
            "ick.m4a",
            "br.m4a",
            "ow.m4a",
            "n.m4a",
            "f.m4a",
            "ox.m4a",
            "ju.m4a",
            "m.m4a",
            "p.m4a",
            "s.m4a",
            "o.m4a",
            "v.m4a",
            "er.m4a",
            "l.m4a",
            "a.m4a",
            "zy.m4a",  
            "d.m4a",
            "og.m4a"];

words = ["the.m4a",
        "quick.m4a",
        "brown.m4a",
        "fox.m4a",
        "jumps.m4a",
        "over.m4a",
        "lazy.m4a",
        "dog.m4a",
]

phonicStrs = []
for (let i = 0; i < phonics.length; i++) {
    phonicStrs[i] = phonics[i].substring(0, phonics[i].length - 4);
}

wordStrs = []
for (let i = 0; i < words.length; i++) {
    wordStrs[i] = words[i].substring(0, words[i].length - 4);
}


function handlePhonicsClick(event) {
    const span = event.target;
    let file = null;

    for (let i = 0; i < phonics.length; i++) {
        if (span.className === phonicStrs[i]) {
            file = phonics[i];
            console.log(phonics[i]);
            break;
        }
    }

    if (file) {
        const audio = new Audio(`../Resources/audio/${file}`);
        audio.play();
        coinCount++;
        document.querySelector('.coins').innerText = coinCount;
    }
}

function handleWordsClick(event) {
    const word = event.target;
    console.log(word)
    let file = null;

    console.log(word.className);

    for (let i = 0; i < words.length; i++) {
        if (word.className === wordStrs[i]) {
            file = words[i];
            console.log(words[i]);
            break;
        }
    }

    if (file) {
        const audio = new Audio(`../Resources/audio/${file}`);
        audio.play();
        coinCount++;
        document.querySelector('.coins').innerText = coinCount;
    }
}


document.querySelector('.toggle').addEventListener('click', (event) => {
    sightWords = !sightWords; // Toggle the boolean value
    console.log(sightWords); // Log the current state
    event.target.innerText = sightWords ? 'Sight Words' : 'Phonics'; // Update the button text

    // Add or remove event listeners for phonics mode
    document.querySelectorAll('.word > span').forEach((span) => {
        if (sightWords) {
            span.addEventListener('click', handlePhonicsClick); // Add event listener for phonics mode
        } else {
            span.removeEventListener('click', handlePhonicsClick); // Remove event listener for phonics mode
        }
    });

    // Add or remove event listeners for sight words mode
    document.querySelectorAll('.word').forEach((word) => {
        if (!sightWords) {
            word.addEventListener('click', handleWordsClick); // Add event listener for sight words mode
        } else {
            word.removeEventListener('click', handleWordsClick); // Remove event listener for sight words mode
        }
    });
});

