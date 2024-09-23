set table "gnuplot/DS03_prive/3.table"; set format "%.5f"
set samples 100.0; set parametric; plot [t=-2:3] [] [] log10(10**t),(t<log10(1/(0.75))? 0:-90)
