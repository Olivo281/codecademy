// Returns a random DNA base
const returnRandBase = () => {
  const dnaBases = ['A', 'T', 'C', 'G'];
  return dnaBases[Math.floor(Math.random() * 4)];
};

// Returns a random single strand of DNA containing 15 bases
const mockUpStrand = () => {
  const newStrand = [];
  for (let i = 0; i < 15; i++) {
    newStrand.push(returnRandBase());
  }
  return newStrand;
};

// Factory function to create a pAequor object
function pAequorFactory(num, arr) {
  return {
    specimenNum: num,
    dna: arr,

    // Method to mutate the DNA
    mutate() {
      const randomIndex = Math.floor(Math.random() * this.dna.length);
      const currentBase = this.dna[randomIndex];
      let newBase;
      do {
        newBase = returnRandBase();
      } while (newBase === currentBase);
      this.dna[randomIndex] = newBase;
      return this.dna;
    },

    // Method to compare DNA sequences with another pAequor
    compareDNA(otherPAequor) {
      let commonCount = 0;
      for (let i = 0; i < this.dna.length; i++) {
        if (this.dna[i] === otherPAequor.dna[i]) {
          commonCount++;
        }
      }
      const percentage = (commonCount / this.dna.length) * 100;
      console.log(`specimen #${this.specimenNum} and specimen #${otherPAequor.specimenNum} have ${percentage.toFixed(2)}% DNA in common.`);
    },

    // Method to check if the organism is likely to survive
    willLikelySurvive() {
      const countCOrG = this.dna.filter(base => base === 'C' || base === 'G').length;
      return (countCOrG / this.dna.length) >= 0.6;
    },

    // Method to return the complementary DNA strand
    complementStrand() {
      const complement = {
        'A': 'T',
        'T': 'A',
        'C': 'G',
        'G': 'C'
      };
      return this.dna.map(base => complement[base]);
    }
  };
}

// Create two pAequor objects
const pAequor1 = pAequorFactory(1, mockUpStrand());
const pAequor2 = pAequorFactory(2, mockUpStrand());

console.log('DNA of pAequor1:', pAequor1.dna);
console.log('DNA of pAequor2:', pAequor2.dna);

// Mutate the DNA of the first pAequor
console.log('Mutating pAequor1...');
pAequor1.mutate();
console.log('Mutated DNA of pAequor1:', pAequor1.dna);

// Compare DNA of the two pAequor objects
pAequor1.compareDNA(pAequor2);

// Check if each pAequor is likely to survive
console.log(`pAequor1 will likely survive: ${pAequor1.willLikelySurvive()}`);
console.log(`pAequor2 will likely survive: ${pAequor2.willLikelySurvive()}`);

// Get and display the complementary DNA strand of each pAequor
console.log('Complementary DNA of pAequor1:', pAequor1.complementStrand());
console.log('Complementary DNA of pAequor2:', pAequor2.complementStrand());

// Generate 30 surviving pAequor instances
const survivingPAequor = [];
let specimenNum = 3; // Start from 3 since 1 and 2 are already created

while (survivingPAequor.length < 30) {
  const newPAequor = pAequorFactory(specimenNum, mockUpStrand());
  if (newPAequor.willLikelySurvive()) {
    survivingPAequor.push(newPAequor);
  }
  specimenNum++;
}

console.log(`Created ${survivingPAequor.length} surviving pAequor specimens.`);
