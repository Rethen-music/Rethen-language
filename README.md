# Rethen-language
Rethen is a modern programming language used to describe musical notation.
Thanks to this, you can create very complex notes in a very simple way.
<br>
<br>

# TOKENS DESCRIPTION:

|token                                           |regex                          |
|-------------------------------                 |-----------------------------  |
| [SOUND](#sound)                                         |<pre>^[c,C,d,D,e,E,f,F,g,G,a,A,h,H][#,b,\\\\,bb,##, \\\\\\\\]?[1-3]?$\|^p$        </pre>|
| [CLEF](#clef)                                           |<pre>\^clef:$</pre>                    |
| [CLEF_VALUE](#clef_value)             | <pre>\^bass$ | \^treble$ <\pre> |
| [KEY](#key)                                             |<pre>\^\[c,C,d,D,e,E,f,F,g,G,a,A,h,H](-sharp\|-flat)(-minor\|-major)$ </pre>  |
| [SOUND_DURATION](#sound_duration)                              |<pre>(\^[1-9][0-9]*[:][1-9][0-9]*)\|^1$ </pre>|
| [TIME_SIGNATURE_VALUE](#time_signature_value)                      |<pre>\^[1-9][0-9]*[//][1-9][0-9]*$    </pre>  |
| [TIME_SIGNATURE](#time_signature)                                 |<pre> ^time signature:$               </pre>   |
| [TAB](#tab)                                      |<pre> (^\t$) \| (^    $)</pre>         |
| [DYNAMICS](#dynamics)                                        |<pre> ^(ppp\|pp\|p\|mp\|mf\|f\|ff\|fff)$  </pre> |
| [ARTICULATION](#articulation)                                     |<pre> ^(staccato\|legato\|portato)$    </pre> |
| [TEMPO](#tempo)                                         |<pre>^(grave\|largo\|lento\|larghetto\|adagio\|andante\|moderato\|andantino\|allegretto\|<br>allegro\|vivo vivace\|presto\|presto vivacissimo\|prestissimo)$ </pre>    |
| [OTHER](#other) |<pre>^(ad libitum\|agitato\|alla\|appassionato\|appena\|assai\|calando\|cantabile\|con\|<br>deciso\|dolce\|dolcissimo\|energico\|eroico\|furioso\|in modo\|lacrimoso\|<br>lamentoso\|leggiero\|maestoso\|malinconico\|marcato\|marciale\|meno\|misterioso\|<br>moderato\|molto\|non molto\|non tanto\|non troppo\|patetico\|più\|quasi\|rigoroso\| <br>saltando\|scherzando\|sempre\|tranquillamente\|trionfante\|vigoroso\|zeloso\|<br>accentuato\|con forza\|con fuoco\|con tutta la forza\|mezza voce\|<br>non troppo\|simile\|sotto voce\|súbito\|tutti\|una corda <br>accelerando\|allargando\|doppio movimento\|meno mosso\|<br>poco un poco\|rallentando\|ritardando\|ritenuto\|<br>sostenuto\|pizzicato\|tremolo\|détaché\|vibrato\|sforzato\|sul tasto)$ </pre>|  
| [STRING](#string) | <pre> ^[A-Za-z]?$</pre>
| [AUTHOR](#author)   | <pre> ^author:$ </pre> |
| [QUOTES](#quotes) | <pre>^"$</pre>|
| [TITLE](#title)  | <pre> ^title:$</pre> |


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
In RetHen there are different kinds of keys:

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
Token for sound

ex.1 1 Line octave
```
g1
e1
e1
f1
d1
d1
c1
e1
g1
```
ex.2 1 Line octave
```

```


## SOUND_DURATION
Token for sound

ex.1 1 Line octave
```
g1
e1
e1
f1
d1
d1
c1
e1
g1
```
ex.2 1 Line octave
```

```

## TIME_SIGNATURE_VALUE
Token for sound

ex.1 1 Line octave
```
g1
e1
e1
f1
d1
d1
c1
e1
g1
```
ex.2 1 Line octave
```

```

## TIME_SIGNATURE
Token for sound

ex.1 1 Line octave
```
g1
e1
e1
f1
d1
d1
c1
e1
g1
```
ex.2 1 Line octave
```

```

## TAB
Token for sound

ex.1 1 Line octave
```
g1
e1
e1
f1
d1
d1
c1
e1
g1
```
ex.2 1 Line octave
```

```

## TIME_SIGNATURE
Token for sound

ex.1 1 Line octave
```
g1
e1
e1
f1
d1
d1
c1
e1
g1
```
ex.2 1 Line octave
```

```

## TIME_SIGNATURE
Token for sound

ex.1 1 Line octave
```
g1
e1
e1
f1
d1
d1
c1
e1
g1
```
ex.2 1 Line octave
```

```

## DYNAMICS
Token for sound

ex.1 1 Line octave
```
g1
e1
e1
f1
d1
d1
c1
e1
g1
```
ex.2 1 Line octave
```

```


## ARTICULATION
Token for sound

ex.1 1 Line octave
```
g1
e1
e1
f1
d1
d1
c1
e1
g1
```
ex.2 1 Line octave
```

```

## TEMPO
Token for sound

ex.1 1 Line octave
```
g1
e1
e1
f1
d1
d1
c1
e1
g1
```
ex.2 1 Line octave
```

```

## OTHER
Token for sound

ex.1 1 Line octave
```
g1
e1
e1
f1
d1
d1
c1
e1
g1
```
ex.2 1 Line octave
```

```

## STRING
Token for sound

ex.1 1 Line octave
```
g1
e1
e1
f1
d1
d1
c1
e1
g1
```
ex.2 1 Line octave
```

```

## AUTHOR
Token for sound

ex.1 1 Line octave
```
g1
e1
e1
f1
d1
d1
c1
e1
g1
```
ex.2 1 Line octave
```

```

## QUOTES
Token for sound

ex.1 1 Line octave
```
g1
e1
e1
f1
d1
d1
c1
e1
g1
```
ex.2 1 Line octave
```

```

## TITLE
Token for sound

ex.1 1 Line octave
```
g1
e1
e1
f1
d1
d1
c1
e1
g1
```
ex.2 1 Line octave
```

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

others:
    | OTHER
    | OTHER others;


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
