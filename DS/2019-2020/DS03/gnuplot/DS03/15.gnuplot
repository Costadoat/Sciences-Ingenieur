set table "gnuplot/DS03/15.table"; set format "%.5f"
set samples 100.0; set parametric; plot [t=-2:3] [] [] log10(10**t),-90+(t<log10(1/(0.0016))? 0:-90)+(t<log10(1/(0.75))? 0:-90)+-(t<log10(1/(0.1))? 0:-90)
