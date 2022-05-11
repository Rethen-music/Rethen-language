# Rethen-language
Rethen is a modern programming language used to describe musical notation.
Thanks to this, you can create very complex notes in a very simple way.
<br>
<br>

## TOKENS:

|token                                           |regex                          |
|-------------------------------                 |-----------------------------  |
|SOUND                                           |<pre>^[c,C,d,D,e,E,f,F,g,G,a,A,h,H][#,b,\\\\]?[1-3]?$\|^p$        </pre>|
|CLEF                                            |<pre>\^clef:$</pre>                    |
|CLEF_VALUE             | <pre>\^bass$ | \^treble$ <\pre> |
|KEY                                             |<pre>\^\[c,C,d,D,e,E,f,F,g,G,a,A,h,H](-sharp\|-flat)(-minor\|-major)$ </pre>  |
|SOUND_DURATION                                |<pre>(\^[1-9][0-9]*[:][1-9][0-9]*)\|^1$ </pre>|
|TIME_SIGNATURE_VALUE                        |<pre>\^[1-9][0-9]*[//][1-9][0-9]*$    </pre>  |
|TIME_SIGNATURE                                 |<pre> ^time signature:$               </pre>   |
|TAB                                       |<pre> (^\t$) \| (^    $)</pre>         |
|DYNAMICS                                        |<pre> ^(ppp\|pp\|p\|mp\|mf\|f\|ff\|fff)$  </pre> |
|ARTICULATION                                    |<pre> ^(staccato\|legato\|portato)$    </pre> |
|TEMPO                                          |<pre>^(grave\|largo\|lento\|larghetto\|adagio\|andante\|moderato\|andantino\|allegretto\|<br>allegro\|vivo vivace\|presto\|presto vivacissimo\|prestissimo)$ </pre>    |
|OTHER |<pre>^(ad libitum\|agitato\|alla\|appassionato\|appena\|assai\|calando\|cantabile\|con\|<br>deciso\|dolce\|dolcissimo\|energico\|eroico\|furioso\|in modo\|lacrimoso\|<br>lamentoso\|leggiero\|maestoso\|malinconico\|marcato\|marciale\|meno\|misterioso\|<br>moderato\|molto\|non molto\|non tanto\|non troppo\|patetico\|più\|quasi\|rigoroso\| <br>saltando\|scherzando\|sempre\|tranquillamente\|trionfante\|vigoroso\|zeloso\|<br>accentuato\|con forza\|con fuoco\|con tutta la forza\|mezza voce\|<br>non troppo\|simile\|sotto voce\|súbito\|tutti\|una corda <br>accelerando\|allargando\|doppio movimento\|meno mosso\|<br>poco un poco\|rallentando\|ritardando\|ritenuto\|<br>sostenuto\|pizzicato\|tremolo\|détaché\|vibrato\|sforzato\|sul tasto)$ </pre>|  
|STRING | <pre> ^[A-Za-z]?$</pre>
|AUTHOR   | <pre> ^author:$ </pre> |
|QUOTES  | <pre>^"$</pre>|
|TITLE   | <pre> ^title:$</pre> |

### TOKENS DESCRIPTION:
SOUND
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
