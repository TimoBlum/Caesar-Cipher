import pygame, random
pygame.init()

x = 1000
y = 400
win = pygame.display.set_mode((x, y))
pygame.display.set_caption("Caesar Cipher")
clock = pygame.time.Clock()
run = True
abc = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890.,?! "
font = pygame.font.Font('freesansbold.ttf', 32)
text, textRect, ntext, ntextRect = "", "", "", ""
key = random.randint(1, 20)


def makeText(txt):
    global text, textRect, ntext, ntextRect, key
    ntxt = ""

    EnDe = input("Do you want to Encrypt or Decrypt (En=0/De=1): ")
    while int(EnDe) < 0 or int(EnDe) > 1:
        EnDe = input("Do you want to Encrypt or Decrypt (En=0/De=1): ")

    while len(txt) > 50:
        print("Too long!")
        txt = input("text: ")

    if int(EnDe) == 1:
        k = input("whats the key: ")
        ntxt = deShiftText(txt, int(k))
    elif int(EnDe) == 0:
        ntxt = shiftText(txt, key)
        print("Encrypted: ", ntxt)
        print("Encryption key: ", key)

    ntext = font.render(ntxt, True, (0, 0, 0))
    text = font.render(txt, True, (0, 0, 0))
    ntextRect = ntext.get_rect()
    ntextRect.center = (x // 2, (y // 2))
    textRect = text.get_rect()
    textRect.center = (x // 2, y // 2-50)


def findPlace(s):
    global abc
    counter = 0
    for i in abc:
        if i == s:
            return counter
        else:
            counter += 1


def shiftText(txt, shift):
    global abc
    newWord = ""
    for i in txt:
        if shift + findPlace(str(i)) > len(abc)-1:
            newWord += abc[(shift + findPlace(str(i)) - len(abc))]
        else:
            newWord += abc[shift + findPlace(str(i))]
    return newWord


def deShiftText(txt, shift):
    global abc
    newWord = ""
    for i in txt:
        if findPlace(i) - shift < 0:
            newWord += abc[-(shift-findPlace(i))]
        else:
            newWord += abc[findPlace(i)-shift]
    return newWord


def redrawGameWin():
    global text, textRect, ntext, ntextRect
    win.fill((255, 255, 255))
    win.blit(text, textRect)
    win.blit(ntext, ntextRect)
    pygame.display.update()


def main():
    global run
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        redrawGameWin()


makeText(input("text: "))
main()
