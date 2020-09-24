class LinearRegression():
    __a = None
    __b = None
    def model(self, x_bill_list, y_tip_list): # create the linearregression given by x, y dataset
        # assume the length of x_bill_list and y_tip_list are the same
        index = 0
        x_sum = 0
        xSquare_sum = 0
        y_sum = 0
        ySquare_sum = 0
        xy_sum = 0
        while (index < len(x_bill_list)): # break out from the while loop when index >= len(x_bill_list)
            x_sum += x_bill_list[index]
            xSquare_sum += (x_bill_list[index])**2
            y_sum += y_tip_list[index]
            ySquare_sum += (y_tip_list[index])**2
            xy_sum += x_bill_list[index]*y_tip_list[index]
            index+=1
        # y = a + bx
        # calculate b
        bSlope = (len(x_bill_list) * xy_sum - x_sum * y_sum) / (len(x_bill_list) * xSquare_sum - (x_sum)**2)
        aIntercept = (y_sum * xSquare_sum - x_sum * xy_sum) / (len(x_bill_list) * xSquare_sum - (x_sum)**2)
        self.__b = bSlope
        self.__a = aIntercept


    def predict(self, new_bill_list): # predict the y values given by new_bill_list using the linear regression result
        result = []

        for index in range(len(new_bill_list)):
            #print(len(new_bill_list))
            #print(new_bill_list[index])
            #print(b * new_bill_list[index] + a)
            result.append(self.__b * new_bill_list[index] + self.__a)
        return result

    def regression_string_2_list(self, my_string):
        result = my_string.split(',')
       

        for i in range(0, len(result)): 
            result[i] = int(result[i]) 
        return result
      

