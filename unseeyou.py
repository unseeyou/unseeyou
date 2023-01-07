from homo_sapiens.alive import unseeyou


def contact_me():
    if unseeyou.status() != "busy":
        return "Hello! I am available for contact."
    else:
        return "Unfortunately I am busy. Ping me on discord if urgent."

      
if __name__ == "__main__":
    contact_me()
    
