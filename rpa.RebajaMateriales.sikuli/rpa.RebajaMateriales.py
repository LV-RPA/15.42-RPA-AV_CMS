import datetime
import os 
import glob
import shutil
desde = datetime.datetime.now() + datetime.timedelta(days=-0)
hasta = datetime.datetime.now()
user_cms = "JCABEL11" 
pass_cms = "Jhoel02201" 
user_inguz = "74590179"
pass_inguz = "jarvis"
link_inguz = "http://www.anovo.pe/inguz"
link_carga = "http://www.anovo.pe/inguz/formRutinas/frmCargaCertificacion.aspx"
rutinas = r'\\10.10.1.250\Desarrollo\cmsFiles\rutinas'
averias = r'\\10.10.1.250\Desarrollo\cmsFiles\averias'
altas = r'\\10.10.1.250\Desarrollo\cmsFiles\altas'
altas2 = r'\\10.120.15.42\cmsFiles\altas'
componentes_lima = r'\\10.10.1.250\Desarrollo\cmsFiles\componentes_lim_det'
contrata445 = r'\\10.10.1.250\Desarrollo\cmsFiles\contrata445'
componentes445_lim_det = r'\\10.10.1.250\Desarrollo\cmsFiles\componentes445_lim_det'
altas_are = r'\\10.10.1.250\Desarrollo\cmsFiles\altas_are'
altas_are2 = r'\\10.120.15.42\cmsFiles\altas_are'
componentes_are_det = r'\\10.10.1.250\Desarrollo\cmsFiles\componentes_are_det'
componentes_are_det2 = r'\\10.120.15.42\cmsFiles\componentes_are_det'
delete_files = r'del /S /Q \\10.10.1.250\Desarrollo\cmsFiles\*'

print(desde)
print(hasta)

print("cerrar procesos")
os.system('taskkill /f /im cms.exe')
os.system('taskkill /f /im te_envot.exe')
os.system('taskkill /f /im te_alav.exe')
os.system('taskkill /f /im te_manot.exe')
os.system('taskkill /f /im firefox.exe')

print("borrar archivos")
os.system(delete_files)

print("Abrir CMS")
App.open("C:\\Gescab\\cms.exe")
sleep(5)
wait(Pattern("1555385646469.png").similar(0.80),1800)

print("modulo encontrado")
paste("1555191515556.png", user_cms)
sleep(2)
type(Key.TAB)
sleep(2)
paste(pass_cms)
type(Key.ENTER)

wait(Pattern("1555191558075.png").similar(0.80),3600)
sleep(2)
type(Key.ENTER)
sleep(2)
click("1555191587121.png")
sleep(2)
click(Pattern("1555191605081.png").targetOffset(6,11))
sleep(2)
click("1555191630786.png")
sleep(2)
wait(Pattern("1555191646245.png").similar(0.80),1800)
sleep(2)

print("listo, cable mágico")
def cambiarusuario():
    type("u",KEY_ALT)
    sleep(1)
    type("s",KEY_ALT)
    sleep(1)

cambiarusuario()
cambiarusuario()
cambiarusuario()
cambiarusuario()
cambiarusuario()

print("abrir modulo")
doubleClick(Pattern("1555191664304.png").targetOffset(-68,2))
sleep(10)
click(Pattern("1555191664304.png").targetOffset(-68,2))
sleep(2)
wait(Pattern("1555191780299.png").similar(0.80),120)
sleep(2)

print("salio en proceso")
click(Pattern("1555191795518.png").targetOffset(-59,0))
sleep(2)
click(Pattern("1580766520888.png").targetOffset(-100,0))
sleep(2)

print("inicio exportar rutinas")
doubleClick(Pattern("1580766550612.png").targetOffset(-73,0))
sleep(2)
wait("1580766645837.png",240)
sleep(2)
click(Pattern("1580766645837.png").targetOffset(30,0))
sleep(2)
type(Pattern("1580766698061.png").targetOffset(26,1), desde.strftime("%d%m%Y"))
sleep(2)
type(Pattern("1580766709322.png").targetOffset(23,1), hasta.strftime("%d%m%Y"))

print("ingresaron las fechas")
click(Pattern("1580766782908.png").targetOffset(-32,-2))
sleep(2)
click(Pattern("1580766819130.png").targetOffset(-30,2))

print("selecciona lima")
sleep(3)
click(Pattern("1580766890036.png").targetOffset(73,-12))
sleep(2)
for step in range(2):
    sleep(2)
    click(Pattern("1580767325635.png").targetOffset(-3,-24))
sleep(3)
click(Pattern("1580767363033.png").targetOffset(-21,2))
sleep(2)
click(Pattern("1580767397405.png").targetOffset(-35,-1))
sleep(2)

print("listo para exportar rutinas")
click(Pattern("1580767427109.png").targetOffset(-39,2))
sleep(2)
wait("1580767480430.png",240)
sleep(2)

print("Data Lista")
click(Pattern("1580767526875.png").targetOffset(0,2))
sleep(2)
click(Pattern("1580767552333.png").targetOffset(121,0))
sleep(2)
click(Pattern("1580767576286.png").targetOffset(-96,0))
sleep(2)
type(Pattern("1580767618248.png").targetOffset(35,0), "rutinas")
sleep(2)
type(Key.TAB)
sleep(2)
type(Key.DOWN)
sleep(2)
type(Key.DOWN)
sleep(2)
type(Key.ENTER)
sleep(2)
type(Key.ENTER)
sleep(2)

print("guardamos el archivo rutinas")
wait("1580768082057.png",60)
sleep(2)
type(Key.ENTER)
sleep(2)
click(Pattern("1580767427109.png").targetOffset(43,2))
sleep(3)

print("inicio exportar liquidados averias")
click(Pattern("1580768175700.png").targetOffset(-55,0))
sleep(2)
click(Pattern("1580768253402.png").targetOffset(-53,1))
sleep(2)
click(Pattern("1580768319418.png").targetOffset(-88,-9))
sleep(2)
doubleClick(Pattern("1580768396442.png").similar(0.80).targetOffset(-71,-8))
sleep(2)
wait("1580768460243.png",240)
sleep(2)
click(Pattern("1580768460243.png").targetOffset(16,0))
sleep(2)

print("Buscar lima averias")
for step in range(4):
    sleep(2)
    click(Pattern("1580768616934.png").targetOffset(-29,-19))

sleep(2)
click(Pattern("1582150169600.png").targetOffset(13,1))
sleep(2)
click(Pattern("1582150282534.png").targetOffset(91,8))
sleep(2)
click(Pattern("1582150324868.png").similar(0.80).targetOffset(93,6))
sleep(2)

print("Seleccionar anovo")
for step in range(89):
    click(Pattern("1582150406310-1.png").similar(0.80).targetOffset(1,-23))
sleep(2)
click(Pattern("1582150642820.png").targetOffset(5,1))
sleep(2)

click(Pattern("1582150988921.png").targetOffset(90,-2))
sleep(2)

print("seleccionar fechas")
type(Pattern("1582151038598.png").similar(0.80).targetOffset(18,3), desde.strftime("%d%m%Y"))
sleep(2)
type(Pattern("1582151061379.png").targetOffset(19,1), hasta.strftime("%d%m%Y"))
sleep(2)
click(Pattern("1582151084252.png").targetOffset(-7,-1))
sleep(2)

print("guardar averias")
wait("1582151377929.png",240)
sleep(2)
click("1582151405049.png")
sleep(2)
click(Pattern("1580767552333.png").targetOffset(121,0))
sleep(2)
click(Pattern("1580767576286.png").targetOffset(-96,0))
sleep(2)
type(Pattern("1580767618248.png").targetOffset(35,0), "liquidado_averias")
sleep(2)
type(Key.ENTER)
sleep(2)
wait("1582151613881.png",240)
sleep(2)
type(Key.ENTER)
sleep(2)
click(Pattern("1582151637926.png").targetOffset(1,-5))
sleep(2)

print("inicio exportar liquidados rutinas")
click(Pattern("1582151729724.png").targetOffset(-83,0))
sleep(2)
doubleClick(Pattern("1582151766995.png").targetOffset(-110,0))
sleep(2)
wait(Pattern("1582151825665.png").targetOffset(-79,-10),240)
sleep(2)
click(Pattern("1582151825665.png").targetOffset(-79,-10))
sleep(2)

print("seleccionar liquidados")
click(Pattern("1582151898162.png").targetOffset(-42,0))
sleep(2)
click(Pattern("1582151942342.png").targetOffset(22,10))
sleep(2)

print("seleccionar anovo")
for step in range(24):
    click(Pattern("1582152018934.png").similar(0.80).targetOffset(-23,-13))
sleep(2)
click(Pattern("1582152083535.png").targetOffset(-22,0))
sleep(2)
click(Pattern("1582152281426.png").targetOffset(-29,1))
sleep(2)

print("seleccionar fechas")
type(Pattern("1582152392858.png").targetOffset(56,-9), desde.strftime("%d%m%Y"))
sleep(2)
type(Pattern("1582152392858.png").targetOffset(56,36), hasta.strftime("%d%m%Y"))
sleep(2)
click(Pattern("1582152442148.png").targetOffset(-2,0))
sleep(2)

print("guardar averias")
wait("1582152613169.png",240)
sleep(2)
click("1582151405049.png")
sleep(2)
click(Pattern("1580767552333.png").targetOffset(121,0))
sleep(2)
click(Pattern("1580767576286.png").targetOffset(-96,0))
sleep(2)
type(Pattern("1580767618248.png").targetOffset(35,0), "liquidado_rutinas")
sleep(2)
type(Key.ENTER)
sleep(2)
wait("1582152813328.png",240)
sleep(2)
type(Key.ENTER)
sleep(2)
click(Pattern("1582152828481.png").targetOffset(-2,2))
sleep(2)

print("cerrar cms")
click(Pattern("1582152877266.png").targetOffset(0,1))
sleep(5)
wait(Pattern("1555389401450.png").similar(0.80),30)
sleep(2)
click(Pattern("1555389401450.png").targetOffset(25,52))
sleep(5)