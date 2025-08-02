var assert = require("assert");
var Calculate =  require('../index.js')

describe('Calculate', () => {
  describe('.factorial', () => {
    it('output of 5! should be equal to 120', () =>{
      //setup
      const input = 5
      const expectedResult = 120
      //exercise
      const result = Calculate.factorial(input)
      //verify
      assert.equal(result,expectedResult)
    });
    it('should be 0', () =>{
      const input = 0
      const expectedResult = 1
      const result = Calculate.factorial(input)
      assert.equal(result,expectedResult)
    });
  });
});