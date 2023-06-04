# Made by Kartik Dixit

flag = True

try:
    import random
    import json
    import os
    import torch
    import time
    from LanguageProcessing import bag_of_words, tokenize
    from NeuralNetwork import NeuralNet
    from jarvis_features import non_input_functions, input_functions, welcome
    from listen import listen
    from speak import speak

except ModuleNotFoundError:
    print("Sorry, This program cannot on your device because dependencies are not installed.\n Please install all dependencies list in requirement.txt.")

if flag:
        
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    with open('chatbot.json') as file:
        file_data = json.load(file)

    File = 'TrainingDataset.pth'
    flag_2 = True
    try:
        data = torch.load(File)

    except FileNotFoundError or FileExistsError:
        speak(" Training file not found \n Please wait around a minute creating training file... ")
        try:
            os.startfile("C:/Users/Kartik/Desktop/Main/train_model.py")
            time.sleep(60)
            try:
                data = torch.load(File)
                speak("Trainig file created sucessfully.")
            except:
                speak("Please wait some more...")
                time.sleep(20)
                try:
                    data = torch.load(File)
                    speak("Trainig file created sucessfully.")
                except:
                    speak("Unable to create trainig file \n An unknown error occured")
                    time.sleep(2)
                    exit()
        except:
            speak("Unable to create trainig file \n An unknown error occured")
            time.sleep(2)
            exit()
            flag_2 = False
    
    if flag_2:


        # Data from pth file -----------

        input_size = data['input_size']
        hidden_size = data['hidden_size']
        output_size = data['output_size']
        model_state = data['model_state']
        tags = data['tags']
        all_words_list = data["all_words"]

        model = NeuralNet(input_size, hidden_size, output_size).to(device)
        model.load_state_dict(model_state)
        model.eval()

        # Jarvis code start

        name = 'Jarvis'

        def main():
            """ Our jarvis main code (Structure) """
            welcome()
            
            while True:
            
                query = listen()
                if query == "none":
                    continue
                if 'bye' in query:
                    speak("Nice to meet you sir , Exiting")
                    exit()
                
                query_ = tokenize(query)
                x = bag_of_words(query_, all_words_list)

                x = x.reshape(1, x.shape[0])
                x = torch.from_numpy(x).to(device)
                output = model(x)
                a, predicted = torch.max(output, dim=1)
                tag = tags[predicted.item()]

                probability = torch.softmax(output, dim=1)
                got_probability = probability[0][predicted.item()]
                
                if got_probability.item() > 0.75:
                    for each in file_data['messages']:
                        if tag == each['tags']:
                            reply = random.choice(each['responses'])
                            reply = str(reply).lower()

                            if tag == 'greeting' or tag == 'about' or tag == 'about jarvis':
                                speak(reply)

                            if tag == 'bye':
                                speak(reply)
                                exit()

                            elif reply == 'time':
                                non_input_functions("time")

                            elif reply == 'date':
                                non_input_functions("date")

                            elif reply == 'day':
                                non_input_functions("day")

                            elif reply == 'internet_speed':
                                non_input_functions("internet_speed")

                            elif reply == 'screenshot':
                                non_input_functions("screenshot")
                            
                            elif reply == 'translate':
                                non_input_functions("translate")
                            
                            elif reply == 'wikipedia':
                                input_functions("wikipedia", query)
                            
                            elif reply == 'google_search':
                                input_functions("google_search", query)
                            
                            elif reply == 'how_to':
                                input_functions("how_to", query)
                            
                            elif reply == 'feedback':
                                input_functions("feedback", query)
                            
                            else:
                                pass
                else:
                    speak("Sorry, Thats Beyond my abilities at the moment")
                    speak("If you wan to give feedback say, ' I have feedback'")


if __name__ == '__main__':

    main()
