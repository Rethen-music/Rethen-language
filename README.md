# Rethen-language
Rethen is a modern programming language used to describe musical notation.
Thanks to this, you can create very complex notes in a very simple way.
<br>
<br>

## TOKENS:

|token                                           |regex                          |
|-------------------------------                 |-----------------------------  |
|SOUND                                           |<pre>\^[c,C,d,D,e,E,f,F,g,G,a,A,h,H][#,b,\\\\]?[1-3]? </pre>|
|CLEF                                            |<pre>\^clef:     </pre>                    |
|CLEF_VALUE             | <pre>\^bass$ | \^treble$ <\pre> |
|KEY                                             |<pre>\^\[c,C,d,D,e,E,f,F,g,G,a,A,h,H](-sharp\|-flat)(-minor\|-major)</pre>  |
|SOUND_DURATION                                |<pre>(\^[1-9][0-9]*[:][1-9][0-9]*)\|^1$ </pre>|
|TIME_SIGNATURE_VALUE                        |<pre>\^[1-9][0-9]*[//][1-9][0-9]*    </pre>  |
|TIME_SIGNATURE                                 |<pre> time signature:               </pre>   |
|TAB                                       |<pre> (^\t$) \| (^    )</pre>         |
|DYNAMICS                                        |<pre> ppp\|pp\|p\|mp\|mf\|f\|ff\|fff  </pre> |
|ARTICULATION                                    |<pre> staccato\|legato\|portato    </pre> |
|TEMPO                                          |<pre>grave\|largo\|lento\|larghetto\|adagio\|andante\|moderato\|andantino\|allegretto\|<br>allegro\|vivo vivace\|presto\|presto vivacissimo\|prestissimo </pre>    |
|OTHER |<pre>^(ad libitum\|agitato\|alla\|appassionato\|appena\|assai\|calando\|cantabile\|con\|<br>deciso\|dolce\|dolcissimo\|energico\|eroico\|furioso\|in modo\|lacrimoso\|<br>lamentoso\|leggiero\|maestoso\|malinconico\|marcato\|marciale\|meno\|misterioso\|<br>moderato\|molto\|non molto\|non tanto\|non troppo\|patetico\|più\|quasi\|rigoroso\| <br>saltando\|scherzando\|sempre\|tranquillamente\|trionfante\|vigoroso\|zeloso\|<br>accentuato\|con forza\|con fuoco\|con tutta la forza\|mezza voce\|<br>non troppo\|simile\|sotto voce\|súbito\|tutti\|una corda <br>accelerando\|allargando\|doppio movimento\|meno mosso\|<br>poco un poco\|rallentando\|ritardando\|ritenuto\|<br>sostenuto\|pizzicato\|tremolo\|détaché\|vibrato\|sforzato\|sul tasto)$ </pre>|  
|STRING | <pre> ^[A-Za-z]?$</pre>
|AUTHOR   | <pre> ^author:$ </pre> |
|QUOTES  | <pre>^"$</pre>|
|TITLE   | <pre> ^title:$</pre> |


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
    | ARTICULATION DYNAMICS TEMPO OTHER
    | DYNAMICS ARTICULATION TEMPO OTHER
    | TEMPO ARTICULATION DYNAMICS OTHER
    | ARTICULATION TEMPO DYNAMICS OTHER
    | DYNAMICS TEMPO ARTICULATION OTHER
    | TEMPO DYNAMICS ARTICULATION OTHER
    | TEMPO DYNAMICS OTHER ARTICULATION
    | DYNAMICS TEMPO OTHER ARTICULATION
    | OTHER TEMPO DYNAMICS ARTICULATION
    | TEMPO OTHER DYNAMICS ARTICULATION
    | DYNAMICS OTHER TEMPO ARTICULATION
    | OTHER DYNAMICS TEMPO ARTICULATION
    | OTHER ARTICULATION TEMPO DYNAMICS
    | ARTICULATION OTHER TEMPO DYNAMICS
    | TEMPO OTHER ARTICULATION DYNAMICS
    | OTHER TEMPO ARTICULATION DYNAMICS
    | ARTICULATION TEMPO OTHER DYNAMICS
    | TEMPO ARTICULATION OTHER DYNAMICS
    | DYNAMICS ARTICULATION OTHER TEMPO
    | ARTICULATION DYNAMICS OTHER TEMPO
    | OTHER DYNAMICS ARTICULATION TEMPO
    | DYNAMICS OTHER ARTICULATION TEMPO
    | ARTICULATION OTHER DYNAMICS TEMPO
    | OTHER ARTICULATION DYNAMICS TEMPO;


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