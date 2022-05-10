## RetHen

# Rethen-language
Rethen is a modern programming language used to describe musical notation.
Thanks to this, you can create very complex notes in a very simple way.










|token                                           |regex                          |
|-------------------------------                 |-----------------------------  |
|SOUND                                           |<pre>\^[c,C,d,D,e,E,f,F,g,G,a,A,h,H][#,b,\\\\]?[1-3]? </pre>|
|CLEF                                            |<pre>\^clef:     </pre>                    |
|KEY                                             |<pre>\^\[c,C,d,D,e,E,f,F,g,G,a,A,h,H](-sharp\|-flat)(-minor\|-major)</pre>  |
|SOUND_DURATION                                  |<pre>(\^[1-9][0-9]*[:][1-9][0-9]*)\|^1$ </pre>|
|TIME_SIGNATURE_VALUE                            |<pre>\^[1-9][0-9]*[//][1-9][0-9]*    </pre>  |
|TIME_SIGNATURE                                  |<pre> time signature:               </pre>   |
|TAB                                             |<pre> (^\t$) \| (^    )</pre>         |
|DYNAMICS                                        |<pre> ppp\|pp\|p\|mp\|mf\|f\|ff\|fff  </pre> |
|ARTICULATION                                    |<pre> staccato\|legato\|portato    </pre> |
|TEMPO                                           |<pre>grave\|largo\|lento\|larghetto\|adagio\|andante\|moderato\|andantino\|allegretto\|<br>allegro\|vivo vivace\|presto\|presto vivacissimo\|prestissimo </pre>    |
|OTHER |<pre>ad libitum\|agitato\|alla\|appassionato\|appena\|assai\|calando\|cantabile\|con\|<br>deciso\|dolce\|dolcissimo\|energico\|eroico\|furioso\|in modo\|lacrimoso\|<br>lamentoso\|leggiero\|maestoso\|malinconico\|marcato\|marciale\|meno\|misterioso\|<br>moderato\|molto\|non molto\|non tanto\|non troppo\|patetico\|più\|quasi\|rigoroso\| <br>saltando\|scherzando\|sempre\|tranquillamente\|trionfante\|vigoroso\|zeloso</pre>
|STRING | <pre> ^[A-Za-z]?$ </pre>|
