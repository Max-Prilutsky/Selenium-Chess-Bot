from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from chess_helper import chessCheater

data_ply = 1

def clickButton(input_XPath):
    time.sleep(1)
    actions = ActionChains(driver)
    btn = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.XPATH, input_XPath)))
    actions.move_to_element(btn).click().perform()

def located(input_XPath):
    try: 
        WebDriverWait(driver, 1).until(
        EC.presence_of_element_located((By.XPATH, input_XPath)))
    except:
        return False
    return True

def startGame():
    clickButton(
        '//button[@data-cy="modal-first-time-button"]')  # start
    time.sleep(.1)
    clickButton(
        '//button[@title = "Choose"]')  # choose
    clickButton(
        '//button[@title = "Play"]')  # play


def movePiece(piece, start, end):
    print(start + end)
    global data_ply, driver
    # click the piece
    clickButton(f'//div[@class = "piece {piece} square-{start}"]')
    # click where it's going
    if located(f'//div[@class = "hint square-{end}"]'):
        clickButton(f'//div[@class = "hint square-{end}"]')
    else:
        clickButton(f'//div[@class = "capture-hint square-{end}"]')
    data_ply += 1


def readMove():
    global data_ply, driver
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, f"//div[@class='black node selected']")))  # opponent has made a move
    highlighted = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "highlight")))
    highlighted = [highlight.get_attribute(
        "class").split(" ") for highlight in highlighted]
    start = highlighted[0][1]
    end = highlighted[1][1]
    return (start, end)


def pieceByEndSquare(end_square):
    try:
        piece = driver.find_elements(By.CLASS_NAME, end_square)[1]
    except:
        piece = driver.find_elements(By.CLASS_NAME, end_square)[0]
    piece = piece.get_attribute("class").split(" ")[1]
    return piece


if __name__ == "__main__":
    global driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.chess.com/play/computer")
    try:
        startGame()
        cheat = chessCheater()
        while not cheat.board.is_game_over():
            move = cheat.get_move()
            movePiece(*move)
            cheat.push_move(*readMove())
    except Exception as e:
        print(e)
    finally:
        print("finished")
        time.sleep(10000)
