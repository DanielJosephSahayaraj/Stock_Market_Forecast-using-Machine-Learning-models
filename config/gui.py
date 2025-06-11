import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import matplotlib.pyplot as plt
from tkinter import messagebox 
import cv2
import pickle

selected_file = None 

def select_file():
    global selected_file
    selected_file = filedialog.askopenfilename()
    print("Selected file:", selected_file)  
    return selected_file

def predict():
    global selected_file
    if selected_file is None:
        messagebox.showerror("Error", "Please select a file first.") 
    else:
        try:
            with open(selected_file, 'rb') as f:
                X_test = pickle.load(f)
        
                    # Load the SVM model
            with open("svm_regressor.pkl", "rb") as file:
                svm_model = pickle.load(file)
            
            # Perform prediction
            prediction = svm_model.predict(X_test)
            # Plotting
            plt.figure()  # Create a new figure
            plt.plot(prediction)
            plt.xlabel("Data Points")
            plt.ylabel("Predicted Values")
            plt.title("Prediction Graph of SVM")
            plt.show()
        
        except FileNotFoundError:
            messagebox.showerror("Error", "File not found.")
        
        except pickle.UnpicklingError as e:
            messagebox.showerror("Error", f"Error occurred while unpickling the file: {str(e)}")
        
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

def orginal_graph():
    with open('X_test.pkl', 'rb') as f:
     X_test = pickle.load(f)

    plt.figure()  # Create a new figure
    plt.plot(X_test, marker='o', linestyle='-',color='green',linewidth=1.5,markersize=1)
    plt.xlabel('Index')
    plt.ylabel('Time-indexed closing stock price')
    plt.title('X_test Data Points')
    plt.grid(True)
    plt.show()


def performance():
    # Define the file paths for the images
    image_path1 = "images/tuned model mape.png"
    image_path2 = "images/tuned model rmse.png"
    image_path3 = "images/untuned model mape.png"
    image_path4 = "images/untuned model rmse.png"

    # Read the first image
    im1_ = cv2.imread(image_path1)
    im2_ = cv2.imread(image_path2)
    im3_ = cv2.imread(image_path3)
    im4_ = cv2.imread(image_path4)

    # Check if either of the images is None
    if im1_ is None or im2_ is None or im3_ is None or im4_ is None:
        print("Error: Unable to read one or both images")
        return

    # Display both images
    cv2.imshow("Image 1", im1_)
    cv2.imshow("Image 2", im2_)
    cv2.imshow("Image 3", im3_)
    cv2.imshow("Image 4", im4_)

    
    # Wait for a key press to close the windows
    cv2.waitKey(0)

    # Close all OpenCV windows
    cv2.destroyAllWindows()





def model_performance():
    # Define the file paths for the images
    image_path1 = "images/actual vs tuned knn.png"
    image_path2 = "images/actual vs tuned decisiontree.png"
    image_path3 = "images/actual vs tuned svm.png"
   

    # Read the first image
    im1_ = cv2.imread(image_path1)
    im2_ = cv2.imread(image_path2)
    im3_ = cv2.imread(image_path3)
    

    # Check if either of the images is None
    if im1_ is None or im2_ is None or im3_ is None:
        print("Error: Unable to read one or both images")
        return

    # Display both images
    cv2.imshow("Image 1", im1_)
    cv2.imshow("Image 2", im2_)
    cv2.imshow("Image 3", im3_)
    

    
    # Wait for a key press to close the windows
    cv2.waitKey(0)

    # Close all OpenCV windows
    cv2.destroyAllWindows()
    

top = tk.Tk()
top.geometry("800x500")
top.resizable(0,0)
top.configure(bg="cyan")

Font = ("Arial", 20, "bold")
label1 = tk.Label(top, text="Stock Price Forecasting", font=Font, bg="cyan", fg="green")
label1.pack(padx=10, pady=5)


Font1=("Arial",10,"bold")
# Button to select a file
select_button = tk.Button(top, text="Select-Test-File",fg="black",width=15,font=Font1,command=select_file)
select_button.place(x=340,y=240)


graph_b=tk.Button(top,text="Actual-Graph",fg="black",width=15,font=Font1,bg="light green",command=orginal_graph)
graph_b.place(x=10,y=70)
# Predict button

performance_b=tk.Button(top,text="performance-graph",fg="black",width=15,font=Font1,bg="light green",command=performance)
performance_b.place(x=10,y=120)

tunedmodel_b=tk.Button(top,text="models-performance",fg="black",width=16,font=Font1,bg="light green",command=model_performance)
tunedmodel_b.place(x=10,y=170)


predict_button = tk.Button(top, text="Predict",font=Font1,width=15, command=predict)
predict_button.place(x=340,y=280)

top.mainloop()
