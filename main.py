import customtkinter
from datetime import datetime
from AA_module import AA_Calculator
import statistics  # bemutatandó + tanult modul

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.title("Havi költség összesítő")
app.geometry("650x820")
app.resizable(False, False)

FONT_CIM = ("Segoe UI", 18, "bold")
FONT_ENTRY = ("Segoe UI", 14)
FONT_RES = ("Segoe UI", 15, "bold")

frame_rezsi = customtkinter.CTkFrame(app, corner_radius=12)
frame_rezsi.pack(padx=20, pady=15, fill="x")

label_rezsi = customtkinter.CTkLabel(
    frame_rezsi,
    text="Rezsiköltségek (Ft/hó)",
    font=FONT_CIM
)
label_rezsi.pack(pady=10)

entry_aram = customtkinter.CTkEntry(frame_rezsi, placeholder_text="Áram", font=FONT_ENTRY, width=400)
entry_aram.pack(pady=5)

entry_gaz = customtkinter.CTkEntry(frame_rezsi, placeholder_text="Gáz", font=FONT_ENTRY, width=400)
entry_gaz.pack(pady=5)

entry_viz = customtkinter.CTkEntry(frame_rezsi, placeholder_text="Víz", font=FONT_ENTRY, width=400)
entry_viz.pack(pady=5)

entry_net = customtkinter.CTkEntry(frame_rezsi, placeholder_text="Internet + TV", font=FONT_ENTRY, width=400)
entry_net.pack(pady=5)

frame_uzemanyag = customtkinter.CTkFrame(app, corner_radius=12)
frame_uzemanyag.pack(padx=20, pady=15, fill="x")

label_uzemanyag = customtkinter.CTkLabel(
    frame_uzemanyag,
    text="Üzemanyag (Ft/hó)",
    font=FONT_CIM
)
label_uzemanyag.pack(pady=10)

entry_tankolas = customtkinter.CTkEntry(frame_uzemanyag, placeholder_text="Havi üzemanyag költség", font=FONT_ENTRY, width=400)
entry_tankolas.pack(pady=5)

frame_egyeb = customtkinter.CTkFrame(app, corner_radius=12)
frame_egyeb.pack(padx=20, pady=15, fill="x")

label_egyeb = customtkinter.CTkLabel(
    frame_egyeb,
    text="Egyéb költségek (Ft/hó)",
    font=FONT_CIM
)
label_egyeb.pack(pady=10)

entry_egyeb = customtkinter.CTkEntry(frame_egyeb, placeholder_text="Egyéb költségek", font=FONT_ENTRY, width=400)
entry_egyeb.pack(pady=5)

frame_res = customtkinter.CTkFrame(app, corner_radius=12)
frame_res.pack(padx=20, pady=20, fill="x")

label_eredmeny = customtkinter.CTkLabel(
    frame_res,
    text="",
    font=FONT_RES,
    justify="left"
)
label_eredmeny.pack(pady=20)

def calc():
    try:
        aram = float(entry_aram.get() or 0)
        gaz = float(entry_gaz.get() or 0)
        viz = float(entry_viz.get() or 0)
        net_tv = float(entry_net.get() or 0)
        tankolas = float(entry_tankolas.get() or 0)
        egyeb = float(entry_egyeb.get() or 0)

        calc_obj = AA_Calculator(aram, gaz, viz, net_tv, tankolas, egyeb)
        havi = calc_obj.AA_total()

        adatok = [aram, gaz, viz, net_tv, tankolas, egyeb]

        atlag = statistics.mean(adatok)
        median = statistics.median(adatok)
        szoras = statistics.stdev(adatok)

        label_eredmeny.configure(
            text=(
                f"Havi összes: {havi:.0f} Ft\n\n"
                f"Átlag: {atlag:.2f} Ft\n"
                f"Medián: {median:.2f} Ft\n"
                f"Szórás: {szoras:.2f}\n\n"
                f"Számítás ideje:\n{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
            )
        )
    except:
        label_eredmeny.configure(text="Hiba: számokat adj meg minden mezőben!")

def uj_szamitas():
    entry_aram.delete(0, "end")
    entry_gaz.delete(0, "end")
    entry_viz.delete(0, "end")
    entry_net.delete(0, "end")
    entry_tankolas.delete(0, "end")
    entry_egyeb.delete(0, "end")
    label_eredmeny.configure(text="")

button_calc = customtkinter.CTkButton(
    app,
    text="SZÁMÍTÁS",
    font=("Segoe UI", 16, "bold"),
    height=40,
    width=200,
    command=calc
)
button_calc.pack(pady=10)

button_reset = customtkinter.CTkButton(
    app,
    text="ÚJ SZÁMÍTÁS",
    font=("Segoe UI", 14),
    height=40,
    width=200,
    command=uj_szamitas,
    fg_color="#bcd9ff",       # halványkék
    hover_color="#a9c9f5",
    text_color="black"
)
button_reset.pack(pady=5)

app.mainloop()
