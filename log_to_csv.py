import csv

with open('./screw-16-log.log') as f:
    lines = f.readlines()
    with open('./result.csv', 'w') as f:
        # create the csv writer
        writer = csv.writer(f)
        writer.writerow(["Epoch", "Train Loss", "Test Loss", "AUROC"])

        test_loss = -100
        train_loss = -100
        auroc = -100

        for line in lines:
            parts = line.strip().split(" ")

            if parts[0] == "Epoch:":
                if parts[3] == "test_loss:":
                    epoch, test_loss = parts[1], parts[-1]
                    epoch = int(epoch) +1
                    # writer.writerow([epoch, "", test_loss])
                else:
                    epoch, train_loss = parts[1], parts[-1]
                    ## check if 1.0, 2.0 etc
                    if int(float(epoch)) == float(epoch) and float(epoch) != 0.0:
                        writer.writerow([epoch, train_loss, test_loss, auroc])
                    else:
                        writer.writerow([epoch, train_loss])

            elif parts[0] == "AUROC:":
                auroc = parts[3]
        
        ### Last epoch
        writer.writerow([epoch, "", test_loss, auroc])