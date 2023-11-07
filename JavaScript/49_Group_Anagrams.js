/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
    const anagrams = {}
    strs.forEach((item) => {
        const sorted = item.split('').sort().join('')
        if (anagrams[sorted]) {
            anagrams[sorted] = [...anagrams[sorted], item]
        } else {
            anagrams[sorted] = [item]
        }
        
    })
    // anagrams = {abt: [bat], ant: [nat, tan]}
    return Object.values(anagrams)
};