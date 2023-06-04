# Made by Kartik
flag = True

try:
    import numpy as np
    import json
    import torch.nn as nn
    import torch
    from torch.utils.data import DataLoader, Dataset
    from LanguageProcessing import stem, tokenize, bag_of_words
    from NeuralNetwork import NeuralNet

except ModuleNotFoundError:
    flag = False
    print("Training is incomplete because some of the modules listed in requirments.txt not installed \n Install all dependencies and then try again ")

if flag:
    print('All dpendencies required for training are installed')

    all_word_list = []
    tags = []
    xy = []
    flag_dataset = True

    try:
        with open('chatbot.json','r') as file:
            messages = json.load(file)

            for msg in messages['messages']:
                tag = msg['tags']
                tags.append(tag)

                for input in msg['patterns']:
                    word = tokenize(input)
                    all_word_list.extend(word)
                    xy.append((word, tag))
    except:
        print("Sorry, Training of model is incomplete as dataset not found")
        flag_dataset = False

    if flag_dataset:
        print("Trainig dataset found...")

        ignore_words_list = ['!','.',',','/','?']

        all_word_list = [stem(word) for word in all_word_list if word not in ignore_words_list]
        all_word_list = sorted(set(all_word_list))
        tags = sorted(set(tags))

        # Traning start from here

        x_train = []
        y_train = []

        for (pattern, tag) in xy:
            bag = bag_of_words(pattern, all_word_list)
            x_train.append(bag)

            label = tags.index(tag)
            y_train.append(label)

            # print(label)
            # print(tags,tag)
        #     print(bag,"\n")
        # print("\n\n",x_train)


        # print("\n\n",y_train)

        x_train = np.array(x_train)
        y_train = np.array(y_train)


        num_epochs = 1000
        batch_size = 8
        learning_rate = 0.001
        input_size = len(x_train[0])
        hidden_size = 8
        output_size = len(tags)

        print("Trainig the model...")

        class ChatDataset(Dataset):
            """ This class gives jarvis ability to learn from experience by the use of database. """

            def __init__(self):
                """ Here we initializes class variables """
                self.num_of_samples = len(x_train)
                self.x_data = x_train
                self.y_data = y_train
            
            def __getitem__(self, index):
                """ It returns values from dataset by their index """
                return self.x_data[index], self.y_data[index]

            def __len__(self):
                """" This function returns int value of no of samples we have.  """
                return self.num_of_samples


        dataset = ChatDataset()
        train_loader = DataLoader(dataset=dataset, batch_size=batch_size, shuffle=True, num_workers=0)

        device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        model = NeuralNet(input_size, hidden_size, output_size).to(device=device)
        criterion = nn.CrossEntropyLoss()
        optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)


        for epoch in range(num_epochs):
            for (words,labels) in train_loader:
                words = words.to(device)
                labels = labels.to(dtype=torch.long).to(device)
                outputs = model(words)
                loss = criterion(outputs, labels)
                optimizer.zero_grad()
                loss.backward()
                optimizer.step()
            
            if (epoch+1) %100 == 0:
                print(f"Epoch [{epoch+1}/{num_epochs}, Loss : {loss.item():.4f}]")

        print(f"Final Loss : {loss.item():.4f}")

        data = {
            "model_state": model.state_dict(),
            "input_size": input_size,
            "hidden_size": hidden_size,
            "output_size": output_size,
            "tags": tags,
            "all_words": all_word_list
        }

        File = 'TrainingDataset.pth'
        torch.save(data, File)

        print("Tranning Completed, \nFile saved to ", File)

else:
    print("Training Incomplete...")


if __name__ == '__main__':
    pass
