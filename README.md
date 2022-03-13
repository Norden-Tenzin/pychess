## about files
# assets 
- holds all the chess pieces. their size changes depending on the size of the board

# py files
- main.py - it does what main does
- constants.py holds all the constants
- makeimagessmaller.py crops the pieces out of the image and resizes it to the board (currently set to 400, 400)
- boardmaker.py intializes the game.txt without any pieces

- compiler.py - TODO - should parse through the game.txt and compute it
- chessman.py - TODO - will hold all the classes for the chessman

# txt files
- game.txt - will hold the text value of the game board

    -   (0,1) - means whether they l r
        Rook = Ro(black) , ro(white)
        Knight = Kn, kn
        Bishop = Bi, bi
        Queen = Qu, qu
        King = Ki, ki 
        Pawn = Pa, pa 
        Empty space = ##

        ## sample board: 

[['a8-Ro' 'b8-Kn' 'c8-Bi' 'd8-Qu' 'e8-Ki' 'f8-Bi' 'g8-Kn' 'h8-Ro']
 ['a7-Pa' 'b7-Pa' 'c7-Pa' 'd7-Pa' 'e7-Pa' 'f7-Pa' 'g7-Pa' 'h7-Pa']
 ['a6-##' 'b6-##' 'c6-##' 'd6-##' 'e6-##' 'f6-##' 'g6-##' 'h6-##']
 ['a5-##' 'b5-##' 'c5-##' 'd5-##' 'e5-##' 'f5-##' 'g5-##' 'h5-##']
 ['a4-##' 'b4-##' 'c4-##' 'd4-##' 'e4-##' 'f4-##' 'g4-##' 'h4-##']
 ['a3-##' 'b3-##' 'c3-##' 'd3-##' 'e3-##' 'f3-##' 'g3-##' 'h3-##']
 ['a2-pa' 'b2-pa' 'c2-pa' 'd2-pa' 'e2-pa' 'f2-pa' 'g2-pa' 'h2-pa']
 ['a1-ro' 'b1-kn' 'c1-bi' 'd1-qu' 'e1-ki' 'f1-bi' 'g1-kn' 'h1-ro']]

 TODO: 
- the piece only moves if its possibel for it to move
- make a write to game.txt method

a8-Ro,b8-Kn,c8-Bi,d8-pa,e8-Ki,f8-Bi,g8-Kn,h8-Ro,
a7-Pa,b7-Pa,c7-Pa,d7-Pa,e7-##,f7-Pa,g7-Pa,h7-Pa,
a6-##,b6-##,c6-##,d6-##,e6-##,f6-##,g6-##,h6-##,
a5-##,b5-##,c5-##,d5-##,e5-##,f5-##,g5-##,h5-##,
a4-##,b4-##,c4-##,d4-##,e4-##,f4-##,g4-##,h4-##,
a3-##,b3-##,c3-##,d3-##,e3-##,f3-##,g3-##,h3-##,
a2-##,b2-##,c2-##,d2-##,e2-##,f2-##,g2-##,h2-##,
a1-##,b1-##,c1-##,d1-qu,e1-##,f1-##,g1-##,h1-##,
