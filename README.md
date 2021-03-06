# Genetic Algorithms to break vignere ciphers

Using 1 alphabet (26 characters) and using a password length of 6 characters gives about 308_915_776(2^26) possiblities to encode a text.

Say you could crack 1000 passwords a second this brings us to about 3000 seconds or 50 minutes to wait for the code to been broken (but with about a 100% certainty).

the Genetic Algorithms using this text takes about 16 generations and 80 seconds to break the code
where as it only cracks about 5 passwords a second with brute force 61_783_155 seconds

That is about 772_289 times faster ;p

The wordlist used comes from [opentaal.nl](https://www.opentaal.org) although it heavily stripped down  
the string used in the POC originates from [wikipedia](https://nl.wikipedia.org/wiki/Biologie) 

To use/ test -> run `Genetic-algorithm-code-breaker.py`

This will prompt for the use of the brute force methode[b] or the genetic algorithm[g].
