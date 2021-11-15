
from evaluation import Evaluation
from voice import Voice


def pronunciation():
    reference = input("Enter your your phase:\n").lower()
    new_voice = Voice()
    sample = new_voice.speaker()

    print(f"Text: {reference}")
    print(f"Speaked: {sample}")

    new_evaluation = Evaluation(reference, sample)

    print("\nResult:")
    print(new_evaluation.compare())
    print("\nGrade:")
    print(new_evaluation.grader())
    print()

menu_options = {
    1: ["Test your speaking", pronunciation],
    2: ["Exit", exit],
}

def print_menu():
    for key in menu_options.keys():
        print (key,"...", menu_options[key][0])
    print()

if __name__=="__main__":
    print("\nSimple app to practce english pronunciation\n")
    while(True):
        print_menu()
        key = ""
        try:
            key = int(input("Enter your option: "))
            
        except:
            print("Unrecognized option, please try again... ")
            
        if key in menu_options: menu_options.get(key, None)[1]()
