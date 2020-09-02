class Color():
    def whiteColor(self, text):
        return "\033[30m%s\033[0m" % text

    def redColor(self, text):
        return "\033[31m%s\033[0m" % text

    def greenColor(self, text):
        return "\033[32m%s\033[0m" % text

    def yellowColor(self, text):
        return "\033[33m%s\033[0m" % text

    def blueColor(self, text):
        return "\033[34m%s\033[0m" % text

    def magentaColor(self, text):
        return "\033[35m%s\033[0m" % text

    def cyanColor(self, text):
        return "\033[36m%s\033[0m" % text

    def greyColor(self, text):
        return "\033[37m%s\033[0m" % text

    def whiteBackground(self, text):
        return "\033[40m%s\033[0m" % text

    def redBackground(self, text):
        return "\033[41m%s\033[0m" % text

    def greenBackground(self, text):
        return "\033[42m%s\033[0m" % text

    def yellowBackground(self, text):
        return "\033[43m%s\033[0m" % text

    def blueBackground(self, text):
        return "\033[44m%s\033[0m" % text

    def magentaBackground(self, text):
        return "\033[45m%s\033[0m" % text

    def cyanBackground(self, text):
        return "\033[46m%s\033[0m" % text

    def greyBackground(self, text):
        return "\033[47m%s\033[0m" % text