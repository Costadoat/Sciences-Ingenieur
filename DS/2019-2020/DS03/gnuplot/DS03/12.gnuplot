set table "gnuplot/DS03/12.table"; set format "%.5f"
set samples 201.0; set parametric; plot [t=-2:3] [] [] log10(10**t),-(t<log10(1/(0.01))? 0:-90)+(t<log10(1/(0.75))? 0:-90)
