# Rethen-language
Rethen is a modern programming language used to describe musical notation.
Thanks to this, you can create very complex notes in a very simple way.
<br>
We use PLY to generate the Scanner and Parser.
<br>

# TOKENS DESCRIPTION:

|token                                           |regex                          |
|-------------------------------                 |-----------------------------  |
| [SOUND_NAME](#sound)|<pre>^[C,D,E,F,G,A,B][#,b,bb,##]?[1-8]?$</pre>|
| [REST](#rest)| <pre>^R$</pre> |
| [SEPARATOR](#separator)|<pre>^,$</pre>|
| [SOUND_DURATION](#sound_duration)|<pre>^([1-9][0-9]?[\\/][1-9][0-9]?\|^1)$</pre>|                                        
| [CLEF](#clef) |<pre>^clef$</pre>|
| [CLEF_VALUE](#clef_value)|<pre>^(treble\|bass\|alto)$ </pre> |
| [KEY](#key) |<pre>^key$</pre>|
| [KEY_VALUE](#key_value)|<pre>\^\[c,C,d,D,e,E,f,F,g,G,a,A,b,B](-sharp\|-flat)?$</pre>|
| [DYMANICS](#dynamics) |<pre>^dynamics$</pre>|
| [DYNAMICS_VALUE](#dynamics_value)|<pre> ^(ppp\|pp\|p\|mp\|mf\|f\|ff\|fff\|sf\|cresc\|decresc\|dim)$</pre>|
| [DESCRIPTION](#description) |<pre>^description$</pre>|
| [QUOTES](#quotes) | <pre>^"$</pre>|
| [STRING](#string) | <pre> ^[A-Za-z][A-Z a-z]*$ </pre> |
| [LYRICS](#lyrics) | <pre> ^lyrics$</pre> |
| [ARTICULATION](#articulation) | <pre> ^articulation$</pre> |
| [ARTICULATION_VALUE](#articulation_value)|<pre> ^(staccato\|legato\|portato\|accent)$</pre> |
| [AUTHOR](#author) | <pre> ^author$ </pre> |
| [TITLE](#title) | <pre>^title$</pre> |
| [TIME_SIGNATURE](#time_signature)|<pre>^time signature:$</pre>|
| [TIME_SIGNATURE_VALUE](#time_signature_value)|<pre>^[1-9][0-9]?[\\/][1-9][0-9]?$</pre>|
| [TAB](#tab)|<pre> (^\t$)\|(^    $)</pre>         |
| [TEMPO](#tempo)| <pre>^tempo$</pre> |
| [CREATE](#create)| <pre>^create$</pre> |
| [PIECE](#piece) |<pre>^piece$</pre> |
| [GROUP](#group) |<pre>^group$</pre> |
| [LINE](#line)| <pre>^line$</pre> |
| [BAR](#bar) |<pre>^bar$</pre> |
| [COLON_SIGN](#colon_sign)|<pre>^:$</pre>|
| [LEFT_SQUARE_BRACKET](#left_square_bracket) |<pre>^[$</pre> |
| [RIGHT_SQUARE_BRACKET](#right_square_bracket)| <pre>^]$</pre> |
| [LEFT_ROUND_BRACKET](#left_square_bracket)| <pre>^($</pre> |
| [RIGHT_ROUND_BRACKET](#right_square_bracket)| <pre>^)$</pre> |
| [REPEAT](#repeat)| <pre>^repeat$</pre> |
| [APPLY](#apply) |<pre>^apply$</pre> |
| [FOR](#for)| <pre>^for$</pre> |
| [AND](#and)| <pre>^&$</pre> |
| [INDEX](#index) |<pre>^i$</pre> |
| [GREATER](#for) |<pre>^>$</pre> |
| [GREATER_EQUALS](#for) |<pre>^>=$</pre> |
| [LOWER](#for)| <pre>^<$</pre> |
| [LOWER_EQUALS](#for)| <pre>^<=$</pre> |
| [EQUALS](#equals_sign) |<pre>^=$</pre>|
| [NUMBER](#number) |<pre>^[0-9][0-9]*$</pre>|



## SOUND
In RetHen a lot of sounds are defined. Each of them belongs to the proper octave:

3 line octave:
```
c3 d3 e3 f3 g3 a3 h3
```
2 line octave:
```
c2 d2 e2 f2 g2 a2 h2
```
1 line octave:
```
c1 d1 e1 f1 g1 a1 h1
```
small octave:
```
c d e f g a h
```
great octave:
```
C D E F G A H
```
contra octave:
```
C1 D1 E1 F1 G1 A1 H1
```
sub-contra octave:
```
C2 D2 E2 F2 G2 A2 H2
```
duble-contra octave:
```
C3 D3 E3 F3 G3 A3 H3
```
Additionally, you can modify sounds by using chromatic signs:

a half-tone upward change (single sharp sign)
```
C#1  
```

a half-tone down change (single flat sign)
```
Cb1 
```

a whole-tone up change (double sharp sign)
```
C##1
```

a whole-tone down change (double flat sign)
```
Cbb1 
```

you can delete a single chromatic sign: (single natural sign)
```
C\2 
```

you can delete duble chromatic sign: (double natural sign) 
```
C\\2 
```


## CLEF
In RetHen there are a lot of keywords, one of them is:
```
clef:
```


## CLEF_VALUE
In RetHen there are different value of clefs:

Treble clef
```
Treble
```

French violin clef
```
French violin
```

Baritone clef
```
Baritone
```

Bass clef
```
Bass
```

Sub-bass clef
```
Sub-bass
```

Alto clef
```
Alto
```

Tenor clef
```
Tenor
```

Soprano clef
```
Soprano
```

Octave clef
```
Octave
```

Neutral clef
```
Neutral
```


Mezzo-soprano clef
```
Mezzo-soprano
```

## KEY
In RetHen, we can use the composition's key:

example 4 types of Keys:
```
C-sharp-minor
C-sharp-major
C-flat-minor
C-flat-major
```

## SOUND_DURATION
In RetHen, we define the duration of the sound:

semibreve
```
1
```
Half note
```
1/2
```
Quarter note
```
1/4
```
Eighth note
```
1/8
```
Sixteenth note
```
1/16
```
Thirty-second note
```
1/32
```
```
ZROBIĆ KROPKA PRZY NUCIE
```

## TIME_SIGNATURE_VALUE
In RetHen, we define value of time signature:

example of time_signature_value:
```
4/4
1/4
2/4
3/4
1/8
3/8
5/8

etc.
```

## TIME_SIGNATURE
In RetHen there are a lot of keywords, one of them is:

Time Signature
```
time_signature:
```


## TAB
In RetHen we use indentation as in Python, we can write with spaces or tabs.

example 1:  one Tab and Sound
```
    c#1
```
example 2: two Tabs and Sound
```
        c#1
```
example 3: 4 spaces and Sound
```
    c#1
```
example 4: 8 spaces and Sound
```
        c#1
```

## DYNAMICS
IN RetHen, we can mark the dynamics:


Pianississimo - As softly as possible
```
ppp
```
Pianissimo - Very softly
```
pp
```
Piano - Softly
```
p
```
Mezzo – Piano Moderately softly
```
mp
```
Mezzo – Forte Moderately loudly
```
mf
```
Forte - Loudly
```
f
```
Fortissimo - Very loudly
```
ff
```
Fortississimo - As loudly as possible
```
fff
```
Sforzando   - sharply accented
```
sf
```
Crescendo   - Gradually louder
```
cresc
```
Decrescendo - Gradually softer
```
decresc
```
Diminuendo  - Gradually softer
```
dim
```


## ARTICULATION
In RetHen, we define the articulation of sounds.

Staccato
```
staccato
```
Legato
```
legato
```
Portato
```
portato
```

## TEMPO
In RetHen, we can define the tempo of the song, we can at the beginning and during the song:

Grave – very slow (25–45 bpm)
```
grave
```
Largo – broadly (40–60 bpm)
```
largo
```
Lento – slowly (45–60 bpm)
```
lento
```
Larghetto – rather broadly (60–66 bpm)
```
larghetto
```
Adagio – slow and stately (literally, "at ease") (66–76 bpm)
```
adagio
```
Andante – at a walking pace (76–108 bpm)
```
andante
```
Andantino – slightly faster than Andante (80–108 bpm)
```
andantino
```
Moderato – moderately (108–120 bpm)
```
moderato
```
Allegretto – moderately fast (112–120 bpm)
```
allegretto
```
Allegro – fast, quickly, and bright (120–168 bpm)
```
allegro
```
vivo-vivace – lively and fast (168–176 bpm)
```
vivo vivace
```
Presto – very, very fast (168–200 bpm)
```
presto
```
presto vivacissimo – very fast and lively (172–176 bpm)
```
presto vivacissimo
```
Prestissimo – even faster than Presto (200 bpm and over)
```
prestissimo
```

## EXECUTION-DESCRIPTION
Description

Examples
```
# TODO
```


## STRING
Description

Examples
```
#TODO
```

## AUTHOR
Description

Examples
```
#TODO
```

## QUOTES
Description

Examples
```
#TODO
```

## TITLE
Description

Examples
```
#TODO
```

## GRAMMAR:

<pre>
%%
newline: 
    | expression EOL;

expression: tabs
    | tabs sound
    | tabs sound_description
    | tabs clef
    | tabs time_signature;
    | tabs KEY;

key: KEY;

time_signature: TIME_SIGNATURE TIME_SIGNATURE_VALUE;


 clef: CLEF CLEF_VALUE;


sound: SOUND sound_description
    | SOUND SOUND_DURATION sound_description;

sound_description:
    | articulation dynamics tempo others
    | dynamics articulation tempo others
    | tempo articulation dynamics others
    | articulation tempo dynamics others
    | dynamics tempo articulation others
    | tempo dynamics articulation others
    | tempo dynamics others articulation
    | dynamics tempo others articulation
    | others tempo dynamics articulation
    | tempo others dynamics articulation
    | dynamics others tempo articulation
    | others dynamics tempo articulation
    | others articulation tempo dynamics
    | articulation others tempo dynamics
    | tempo others articulation dynamics
    | others tempo articulation dynamics
    | articulation tempo others dynamics
    | tempo articulation others dynamics
    | dynamics articulation others tempo
    | articulation dynamics others tempo
    | others dynamics articulation tempo
    | dynamics others articulation tempo
    | articulation others dynamics tempo
    | others articulation dynamics tempo;


articulation:
    | ARTICULATION;

dynamics:
    | DYNAMICS;

tempo:
    | TEMPO;

execution-descriptions:
    | EXECUTION-DESCRIPTION
    | EXECUTION-DESCRIPTION execution-descriptions;


tabs: 
    | TAB
    | TAB tabs;

author: AUTHOR name;

name: QUOTES strings QUOTES;

title: QUOTES strings QUOTES;

strings: STRING
    | STRING strings;

%%
</pre>
