set table "gnuplot/DS03/5.table"; set format "%.5f"
set samples 50.0; set parametric; plot [t=-2:3] [] [] log10(10**t),20*log10(abs(1*sqrt(1+(0.01*10**t)**2)))
