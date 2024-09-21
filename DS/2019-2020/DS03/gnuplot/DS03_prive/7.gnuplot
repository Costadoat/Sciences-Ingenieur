set table "gnuplot/DS03_prive/7.table"; set format "%.5f"
set samples 50.0; set parametric; plot [t=-2:3] [] [] log10(10**t),--180/3.1415957*atan(0.01*10**t)
