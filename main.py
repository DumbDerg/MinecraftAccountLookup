import ttkbootstrap as tk
import util


def main():
    window = tk.Window(themename="darkly")
    window.title("Minecraft Account Lookup")
    img = tk.PhotoImage(file="resources/icon.png")
    window.iconphoto(False, img)
    window.resizable(0, 0)
    window.geometry("620x430")

    userInput = tk.StringVar(window)

    def addInfo(player):
        for widget in frame1.winfo_children():
            widget.destroy()
        label = tk.Label(frame1, text="Minecraft Account Lookup", font="Calibri 12")
        label.grid(row=0, column=0)
        entry = tk.Entry(frame1, textvariable=userInput, width=35)
        entry.grid(row=1, column=0)
        searchButton = tk.Button(frame1, text="Search", command=search)
        searchButton.grid(row=1, column=1)
        uuidLabel = tk.Label(frame1, text="UUID: "+str(player.uuid))
        uuidLabel.grid(row=2,column=0)
        nameLabel = tk.Label(frame1, text="Name: "+str(player.name))
        nameLabel.grid(row=3,column=0)
        downloadButton = tk.Button(frame1, text="Download Skin", command=lambda: download(player))
        downloadButton.grid(row=4,column=0)

    def search():
        if util.checkIfValid(userInput.get()):
            p = util.getPlayerInfo(userInput.get())
            p.skin.skin.save(fp="resources/skin.png")
            skin = tk.PhotoImage(file="resources/skin.png")
            for widget in frame2.winfo_children():
                widget.destroy()
            skinLabel = tk.Label(frame2, image=skin)
            skinLabel.image = skin
            skinLabel.grid(row=0,column=0)
            addInfo(p)
        else:
            label2 = tk.Label(frame1, text="Name/UUID Not Found", font="Calibri 10")
            label2.grid(row=5,column=0)
            window.after(3000, label2.destroy)


    def download(player):
        downloading = tk.Label(frame1, text="Downloading "+player.name+".png!", font="Calibri 10")
        downloading.grid(row=5, column=0)
        window.after(3000, downloading.destroy)
        util.downloadSkin(player)



    frame1= tk.Frame(window)
    frame1.grid(row=0,column=0,sticky="nsew")
    frame2 = tk.Frame(window)
    frame2.grid(row=0, column=1,sticky="nsew")
    label = tk.Label(frame1, text="Minecraft Account Lookup", font="Calibri 12")
    label.grid(row=0,column=0)
    entry = tk.Entry(frame1, textvariable=userInput, width=37)
    entry.grid(row=1,column=0)
    searchButton = tk.Button(frame1, text="Search", command=search)
    searchButton.grid(row=1,column=1)
    #Steve Default Skin
    steve = tk.PhotoImage(file="resources/default.png")
    skinLabel = tk.Label(frame2, image=steve)
    skinLabel.image = steve
    skinLabel.grid(row=0, column=0)
    #addInfo() Stuff
    uuidLabel = tk.Label(frame1, text="UUID:")
    uuidLabel.grid(row=2, column=0)
    nameLabel = tk.Label(frame1, text="Name:")
    nameLabel.grid(row=3, column=0)
    downloadButton = tk.Button(frame1, text="Download Skin")
    downloadButton.grid(row=4, column=0)
    window.mainloop()


if __name__ == '__main__':
    main()