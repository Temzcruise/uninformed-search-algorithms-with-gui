import collections
import tkinter as tk
from tkinter import messagebox


class TreeNode:
    def __init__(self, val="", left=None, right=None, level=0):
        self.val = val
        self.left = left
        self.right = right
        self.level = level


class UninformedAgorithms:
    def __init__(self, window, root, canvas_width, canvas_height):
        self.window = window
        self.root = root
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height
        self.canvas = tk.Canvas(window, bg = "grey", width=canvas_width, height=canvas_height)

        #GUI components
        self.circleA = self.canvas.create_oval(360, 50, 430, 115, fill="white", outline='grey')
        self.textA = self.canvas.create_text(395, 85, fill='black', font='Helvetica 20 bold', text='A')

        self.circleB = self.canvas.create_oval(230, 180, 300, 250, fill="white", outline='grey')
        self.textB = self.canvas.create_text(265, 215, fill='black', font='Helvetica 20 bold', text='B')

        self.circleC = self.canvas.create_oval(480, 180, 550, 250, fill="white", outline='grey')
        self.textC = self.canvas.create_text(515, 215, fill='black', font='arial 20 bold', text='C')

        self.circleD = self.canvas.create_oval(130, 310, 200, 380, fill="white", outline='grey')
        self.textD = self.canvas.create_text(165, 345, fill='black', font='Times 20 bold', text='D')

        self.circleE = self.canvas.create_oval(305, 310, 375, 380, fill="white", outline='grey')
        self.textE = self.canvas.create_text(340, 345, fill='black', font='Times 20 bold', text='E')

        self.circleF = self.canvas.create_oval(420, 310, 490, 380, fill="white", outline='grey')
        self.textF = self.canvas.create_text(455, 345, fill='black', font='Times 20 bold', text='F')

        self.circleG = self.canvas.create_oval(560, 310, 630, 380, fill="white", outline='grey')
        self.textG = self.canvas.create_text(595, 345, fill='black', font='Times 20 bold', text='G')

        self.circleH = self.canvas.create_oval(30, 450, 100, 520, fill="white", outline='grey')
        self.textH = self.canvas.create_text(65, 485, fill='black', font='Times 20 bold', text='H')

        self.circleI = self.canvas.create_oval(200, 450, 270, 520, fill="white", outline='grey')
        self.textI = self.canvas.create_text(235, 485, fill='black', font='Times 20 bold', text='I')

        self.circleJ = self.canvas.create_oval(350, 450, 425, 520, fill="white", outline='grey')
        self.textJ = self.canvas.create_text(385, 485, fill='black', font='Times 20 bold', text='J')

        self.canvas.create_line(395, 115, 290, 190, arrow=tk.LAST, fill="black")  # A to B
        self.canvas.create_line(395, 115, 500, 180, arrow=tk.LAST, fill="black")  # A to C

        self.canvas.create_line(260, 250, 335, 310, arrow=tk.LAST, fill="black")  # B to E
        self.canvas.create_line(260, 250, 185, 320, arrow=tk.LAST, fill="black")  # B to D

        self.canvas.create_line(510, 250, 580, 315, arrow=tk.LAST, fill="black")  # C to G
        self.canvas.create_line(510, 250, 455, 310, arrow=tk.LAST, fill="black")  # C to F

        self.canvas.create_line(160, 380, 230, 450, arrow=tk.LAST, fill="black")  # D to I
        self.canvas.create_line(160, 380, 90,  450, arrow=tk.LAST, fill="black")  # D to H

        self.canvas.create_line(450, 380, 395, 450, arrow=tk.LAST, fill="black")  # F to J

        self.usa = tk.Label(window, text="Uninformed Search Algorithms", bg = "grey", font = "Helvetica 17 bold italic")
        self.usa.place(x=700, y=70)

        self.searchNodeLabel = tk.Label(window, text='Input node to be found', bg = "grey", font=('calibre', 14, 'bold'))
        self.searchNodeLabel.place(x=795, y=125)

        searchNode = tk.StringVar()

        searchEntry = tk.Entry(window, textvariable=searchNode, width=4, font=('calibre', 10, 'normal'))
        searchEntry.place(x=750, y=127)
        searchEntry.focus_set() #set focus to input box

        def to_uppercase(*args): #capitalize input text
            searchNode.set(searchNode.get().upper())
        searchNode.trace_add('write', to_uppercase)


        self.searchBTN = tk.Button(self.window, height = 2, width = 15, text="Search", background="green", fg="white", font='arial 10 bold', command= lambda : runAlgo())
        self.searchBTN.place(x=725, y=470)

        self.resetBTN = tk.Button(self.window, height=2, width=15, text="Reset", background="black", fg="white", font='arial 10 bold', command=lambda: resetAll())
        self.resetBTN.place(x=890, y=470)

        depthLimitedLevelEntry = tk.Entry(window, width=4, font=('calibre', 10, 'normal'))
        depthLimitedLevelEntry.place(x=998, y=304)

        def runAlgo():
            radSel = radVar.get()
            if radSel == 1:   breadthFirstSearch(searchNode.get())
            elif radSel == 2: depthFirstSearch(searchNode.get())
            elif radSel == 3: depthLimitedSearch(searchNode.get(), int(depthLimitedLevelEntry.get()))
            elif radSel == 4: iterativeDeepeningSearch(searchNode.get())

        # radio buttons for algorithm selection
        radVar = tk.IntVar()
        rad1 = tk.Radiobutton(window, text= "Breadth First Search", bg = "grey", variable = radVar, value=1, font=('calibre', 11, 'bold'))
        rad1.place(x=755, y=220)

        rad2 = tk.Radiobutton(window, text="Depth First Search", bg = "grey", variable=radVar, value=2, font=('calibre', 11, 'bold'))
        rad2.place(x=755, y=260)

        rad3 = tk.Radiobutton(window, text="Depth Limited Search - Level: ", bg = "grey", variable=radVar, value=3, font=('calibre', 11, 'bold'))
        rad3.place(x=755, y=300)

        rad4 = tk.Radiobutton(window, text="Iterative Deepening Search", bg = "grey", variable=radVar, value=4, font=('calibre', 11, 'bold'))
        rad4.place(x=755, y=340)

        self.canvas.pack()

        #BREADTH FIRST SEARCH
        def breadthFirstSearch(searchNode):
            queue_ = collections.deque()   #declare queue
            visited = []
            queue_.append(root)     #push root node to queue

            while queue_:
                queue_length = len(queue_)

                for i in range(queue_length):
                    node = queue_.popleft()
                    if node and (node.val == searchNode):
                        visited.append(node.val)
                        break
                    elif node:
                        visited.append(node.val)  #push node to visited
                        queue_.append(node.left)  #push node's left child to queue
                        queue_.append(node.right) #push node's right child to queue

                if visited[-1] == searchNode:
                    break

            self.searchVisualizer(visited, searchNode)

        # DEPTH FIRST SEARCH
        def depthFirstSearch(searchNode):
            stack = []
            visited = []
            stack.append(root)

            while len(stack) != 0:
                newNode = stack.pop()
                if newNode.val not in visited:
                    visited.append(newNode.val)
                if newNode.val == searchNode:
                    break
                children = []
                if newNode.right:
                    children.append(newNode.right)
                if newNode.left:
                    children.append(newNode.left)
                for child in children:
                    if child.val not in visited:
                        stack.append(child)

            self.searchVisualizer(visited, searchNode)

        # DEPTH LIMITED SEARCH
        def depthLimitedSearch(searchNode, level):
            stack = []
            visited = []
            stack.append(root)

            while len(stack) != 0:
                newNode = stack.pop()
                if newNode.val not in visited and newNode.level <= level:
                    visited.append(newNode.val)
                if newNode.val == searchNode:
                    break
                children = []
                if newNode.right and newNode.right.level <= level:
                    children.append(newNode.right)
                if newNode.left and newNode.left.level <= level:
                    children.append(newNode.left)
                for child in children:
                    if child.val not in visited:
                        stack.append(child)

            self.searchVisualizer(visited, searchNode)

        # ITERATIVE DEEPENING SEARCH
        def iterativeDeepeningSearch(searchNode):
            colors = ['orange', 'blue','deep pink', 'purple']

            for i in range(4):
                found = False
                level = i
                level += 1
                stack = []
                visited = []
                stack.append(root)

                while len(stack) != 0:
                    newNode = stack.pop()
                    if newNode.val not in visited and newNode.level < level:
                        visited.append(newNode.val)
                    if newNode.val == searchNode:
                        found = True
                        break
                    children = []
                    if newNode.right and newNode.right.level < level:
                        children.append(newNode.right)
                    if newNode.left and newNode.left.level < level:
                        children.append(newNode.left)
                    for child in children:
                        if child.val not in visited:
                            stack.append(child)

                self.IDDSVisualizer(visited, searchNode, colors[i])
                if found == True:
                    break
                else:
                    continue

            return

        # RESET UI
        def resetAll():
            list_of_nodes = ['A','B','C','D','E','F','G','H','I','J']
            node_mapper = {'A': self.circleA, 'B': self.circleB, 'C': self.circleC,
                           'D': self.circleD, 'E': self.circleE, 'F': self.circleF, 'G': self.circleG,
                           'H': self.circleH, 'I': self.circleI,
                           'J': self.circleJ}

            for i in list_of_nodes:
                self.window.after(0, self.canvas.itemconfig(node_mapper[i], fill='white'))
                self.canvas.update()

    def searchVisualizer(self, list_of_nodes, searchNode):
        node_mapper = {'A': self.circleA, 'B': self.circleB, 'C': self.circleC,
                       'D': self.circleD, 'E': self.circleE, 'F': self.circleF, 'G': self.circleG,
                       'H': self.circleH, 'I': self.circleI, 'J': self.circleJ}

        for i in list_of_nodes:
            self.window.after(500, self.canvas.itemconfig(node_mapper[i], fill="#FFD700"))
            self.canvas.update()

        if list_of_nodes[-1] == searchNode:
            self.window.after(100, self.canvas.itemconfig(node_mapper[list_of_nodes[-1]], fill="green"))
            messagebox.showinfo("showinfo", "Node found")
        else:
            messagebox.showerror("showerror", "Node doesn't exist")

        self.canvas.update()
        return

    def IDDSVisualizer(self, list_of_nodes, searchNode, color):

        node_mapper = {'A': self.circleA, 'B': self.circleB, 'C': self.circleC,
                       'D': self.circleD, 'E': self.circleE, 'F': self.circleF, 'G': self.circleG,
                       'H': self.circleH, 'I': self.circleI,
                       'J': self.circleJ}

        for i, val in enumerate(list_of_nodes):
            self.window.after(700, self.canvas.itemconfig(node_mapper[val], fill=color))
            self.canvas.update()

        if list_of_nodes[-1] == searchNode:
            self.window.after(100, self.canvas.itemconfig(node_mapper[list_of_nodes[-1]], fill="green"))
            messagebox.showinfo("showinfo", "Node found")
            return
        elif i == 9:
            messagebox.showerror("showerror", "Node doesn't exist")

        self.canvas.update()
        return

window = tk.Tk()
window.title("Uninformed search algorithms")
root = TreeNode("A", TreeNode("B", TreeNode("D", TreeNode("H", None, None,3), TreeNode("I", None, None,3),2), TreeNode("E", None, None,2),1), TreeNode("C", TreeNode("F", TreeNode("J", None, None,3), None, 2), TreeNode("G", None, None,2),1),0)
UIA = UninformedAgorithms(window, root, canvas_width=1100, canvas_height=650)
window.mainloop()
