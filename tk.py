from tkinter import *
from tkinter import messagebox
import clear as c

root = Tk()
root.geometry("400x400")
root.title("Notion Clear Trash")
root.eval('tk::PlaceWindow . center')


def clear():
    try:
        token = inputtxt.get(1.0, END).replace('\n', '')
        if len(token) == 0:
            messagebox.showwarning(title="Warning!", message="Your Token v2 is Empty!", )

        else:
            client = c.NotionClient(token_v2=token)
            block_ids = c.get_trash(client)
            c.delete_permanently(client=client, block_ids=block_ids)
            print("SUCCESS")
            messagebox.showinfo(title="Succeeded!", message="Your trash box is cleaned!", )
    except Exception as e:
        print(e)
        messagebox.showwarning(title="Warning!", message="Your Token v2 is Wrong!", )

    # print(input_value)


l = Label(text="Please Enter your token_v2")
inputtxt = Text(root, height=10,
                width=25,
                bg="light yellow")
items = Listbox(root, width=100)

items.insert(0, "1. Go to notion.so")
items.insert(1, "2. Open developer tools (hit F12)")
items.insert(2, "3. Navigate to the Application tab (may be hidden if the developer window is small)")
items.insert(3, "4. Expand Cookies under the Storage section on the sidebar")
items.insert(4, "5. Click on 'https://www.notion.so' to view all the cookies")
items.insert(4, "6. Copy the value for the key 'token_v2'")

items.pack()

l.pack()
inputtxt.pack()
Button(root, text="Clear", command=clear).place(x=200, y=350, anchor=CENTER)

root.mainloop()
