class AA_Calculator:
    def __init__(self, aram, gaz, viz, net_tv, tankolas, egyeb):
        self.aram = aram
        self.gaz = gaz
        self.viz = viz
        self.net_tv = net_tv
        self.tankolas = tankolas
        self.egyeb = egyeb

    def AA_total(self):
        havi_osszes = (
            self.aram +
            self.gaz +
            self.viz +
            self.net_tv +
            self.tankolas +
            self.egyeb
        )

        return havi_osszes
