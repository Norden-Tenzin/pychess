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
- the piece only moves if its possibel for it to move DONE
- make a write to game.txt method DONE

-- sample 
a8-Ro,b8-Kn,c8-Bi,d8-pa,e8-Ki,f8-Bi,g8-Kn,h8-Ro,
a7-Pa,b7-Pa,c7-Pa,d7-Pa,e7-##,f7-Pa,g7-Pa,h7-Pa,
a6-##,b6-##,c6-##,d6-##,e6-##,f6-##,g6-##,h6-##,
a5-##,b5-##,c5-##,d5-##,e5-##,f5-##,g5-##,h5-##,
a4-##,b4-##,c4-##,d4-##,e4-##,f4-##,g4-##,h4-##,
a3-##,b3-##,c3-##,d3-##,e3-##,f3-##,g3-##,h3-##,
a2-##,b2-##,c2-##,d2-##,e2-##,f2-##,g2-##,h2-##,
a1-##,b1-##,c1-##,d1-qu,e1-##,f1-##,g1-##,h1-##,

arial
arialblack
bahnschrift
calibri
cambriacambriamath
cambria
candara
comicsansms
consolas
constantia
corbel
couriernew
ebrima
franklingothicmedium
gabriola
gadugi
georgia
impact
inkfree
javanesetext
leelawadeeui
leelawadeeuisemilight
lucidaconsole
lucidasans
malgungothic
malgungothicsemilight
microsofthimalaya
microsoftjhengheimicrosoftjhengheiui
microsoftjhengheimicrosoftjhengheiuibold
microsoftjhengheimicrosoftjhengheiuilight
microsoftnewtailue
microsoftphagspa
microsoftsansserif
microsofttaile
microsoftyaheimicrosoftyaheiui
microsoftyaheimicrosoftyaheiuibold
microsoftyaheimicrosoftyaheiuilight
microsoftyibaiti
mingliuextbpmingliuextbmingliuhkscsextb
mongolianbaiti
msgothicmsuigothicmspgothic
mvboli
myanmartext
nirmalaui
nirmalauisemilight
palatinolinotype
segoemdl2assets
segoeprint
segoescript
segoeui
segoeuiblack
segoeuiemoji
segoeuihistoric
segoeuisemibold
segoeuisemilight
segoeuisymbol
simsunnsimsun
simsunextb
sitkasmallsitkatextsitkasubheadingsitkaheadingsitkadisplaysitkabanner
sitkasmallsitkatextboldsitkasubheadingboldsitkaheadingboldsitkadisplayboldsitkabannerbold
sitkasmallsitkatextbolditalicsitkasubheadingbolditalicsitkaheadingbolditalicsitkadisplaybolditalicsitkabannerbolditalic
sitkasmallsitkatextitalicsitkasubheadingitalicsitkaheadingitalicsitkadisplayitalicsitkabanneritalic
sylfaen
symbol
tahoma
timesnewroman
trebuchetms
verdana
webdings
wingdings
yugothicyugothicuisemiboldyugothicuibold
yugothicyugothicuilight
yugothicmediumyugothicuiregular
yugothicregularyugothicuisemilight
holomdl2assets
agencyfb
algerian
bookantiqua
arialrounded
baskervilleoldface
bauhaus93
bell
bernardcondensed
bodoni
bodoniblack
bodonicondensed
bodonipostercompressed
bookmanoldstyle
bradleyhanditc
britannic
berlinsansfb
berlinsansfbdemi
broadway
brushscript
bookshelfsymbol7
californianfb
calisto
castellar
centuryschoolbook
centaur
century
chiller
colonna
cooperblack
copperplategothic
curlz
dubai
dubaimedium
dubairegular
elephant
engravers
erasitc
erasdemiitc
erasmediumitc
felixtitling
forte
franklingothicbook
franklingothicdemi
franklingothicdemicond
franklingothicheavy
franklingothicmediumcond
freestylescript
frenchscript
footlight
garamond
gigi
gillsans
gillsanscondensed
gillsansultracondensed
gillsansultra
gloucesterextracondensed
gillsansextcondensed
centurygothic
goudyoldstyle
goudystout
harlowsolid
harrington
haettenschweiler
hightowertext
imprintshadow
informalroman
blackadderitc
edwardianscriptitc
kristenitc
jokerman
juiceitc
kunstlerscript
widelatin
lucidabright
lucidacalligraphy
leelawadee
lucidafaxregular
lucidafax
lucidahandwriting
lucidasansregular
lucidasansroman
lucidasanstypewriterregular
lucidasanstypewriter
lucidasanstypewriteroblique
magneto
maiandragd
maturascriptcapitals
mistral
modernno20
microsoftuighur
monotypecorsiva
extra
niagaraengraved
niagarasolid
ocraextended
oldenglishtext
onyx
msoutlook
palacescript
papyrus
parchment
perpetua
perpetuatitling
playbill
poorrichard
pristina
rage
ravie
msreferencesansserif
msreferencespecialty
rockwellcondensed
rockwell
rockwellextra
script
showcardgothic
snapitc
stencil
twcen
twcencondensed
twcencondensedextra
tempussansitc
vinerhanditc
vivaldi
vladimirscript
wingdings2
wingdings3
acaslonproboldopentype
acaslonprobolditalicopentype
acaslonproitalicopentype
acaslonproregularopentype
acaslonprosemiboldopentype
acaslonprosemibolditalicopentype
adobefangsongstdregularopentype
adobefanheitistdboldopentype
adobegothicstdboldopentype
adobeheitistdregularopentype
adobekaitistdregularopentype
adobenaskhmediumopentype
agaramondproboldopentype
agaramondprobolditalicopentype
agaramondproitalicopentype
agaramondproregularopentype
birchstdopentype
blackoakstdopentype
brushscriptstdopentype
chaparralproboldopentype
chaparralprobolditopentype
chaparralproitalicopentype
chaparralprolightitopentype
chaparralproregularopentype
charlemagnestdboldopentype
hobostdopentype
kozgoproboldopentype
kozgoproextralightopentype
kozgoproheavyopentype
kozgoprolightopentype
kozgopromediumopentype
kozgoproregularopentype
kozminproboldopentype
kozminproextralightopentype
kozminproheavyopentype
kozminprolightopentype
kozminpromediumopentype
kozminproregularopentype
lithosproblackopentype
lithosproregularopentype
minionproboldcnopentype
minionproboldcnitopentype
minionpromediumopentype
minionpromediumitopentype
minionprosemiboldopentype
minionprosemibolditopentype
myriadarabicopentype
nuevastdboldopentype
nuevastdboldcondopentype
nuevastdcondopentype
nuevastditalicopentype
ocrastdopentype
oratorstdopentype
poplarstdopentype
prestigeelitestdbdopentype
sourcesansproblackopentype
sourcesansproopentype
sourcesansproextralightopentype
sourcesansprosemiboldopentype
tektonproboldopentype
tektonproboldcondopentype
tektonproboldextopentype
tektonproboldoblopentype
trajanpro3opentype
adobearabicboldopentype
adobearabicbolditalicopentype
adobearabicitalicopentype
adobearabicregularopentype
adobedevanagariboldopentype
adobedevanagaribolditalicopentype
adobedevanagariitalicopentype
adobedevanagariregularopentype
adobegurmukhiopentype
adobehebrewboldopentype
adobehebrewbolditalicopentype
adobehebrewitalicopentype
adobehebrewregularopentype
adobemingstdlightopentype
adobemyungjostdmediumopentype
adobesongstdlightopentype
kozgopr6nboldopentype
kozgopr6nextralightopentype
kozgopr6nheavyopentype
kozgopr6nlightopentype
kozgopr6nmediumopentype
kozgopr6nregularopentype
kozminpr6nboldopentype
kozminpr6nextralightopentype
kozminpr6nheavyopentype
kozminpr6nlightopentype
kozminpr6nmediumopentype
kozminpr6nregularopentype
lettergothicstdboldopentype
lettergothicstdboldslantedopentype
lettergothicstdslantedopentype
lettergothicstdopentype
minionproboldopentype
minionprobolditopentype
minionproitopentype
minionproregularopentype
myriadhebrewopentype
myriadproboldopentype
myriadproboldcondopentype
myriadproboldconditopentype
myriadprobolditopentype
myriadprocondopentype
myriadproconditopentype
myriadproitopentype
myriadproregularopentype
myriadprosemiboldopentype
myriadprosemibolditopentype