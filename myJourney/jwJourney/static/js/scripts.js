const funFacts = [
    "I love coding while listening to music.",
    "I once built a mini Django app in one weekend!",
    "I enjoy teaching others about technology.",
    "My favorite language is Python because it's fun and readable."
];

function showFunFact() {
    const fact = funFacts[Math.floor(Math.random() * funFacts.length)];
    document.getElementById('funFact').innerText = fact;
}