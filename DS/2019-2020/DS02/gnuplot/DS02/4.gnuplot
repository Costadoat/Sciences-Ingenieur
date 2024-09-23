set table "gnuplot/DS02/4.table"; set format "%.5f"
set samples 100.0; set parametric; plot [t=-2:5] [] [] log10(10**t),-90+(t<log10(1/(.01))? 0:-90)+(t<log10(1/(.0001))? 0:-90)
