def sample_Z(m, n, z_sample, np):
  return np.random.uniform(0., z_sample, size = [m, n]) 

def optimizer(test_all, Dim, testM, testX, No, Missing, Data, fn_ref_csv, New_X_mb, MSE_test_loss, G_sample, New_X, prop_df_one_hot, is_auto_categorical, pd, label, df, features, fn_ocsv, real_test_No, test_Missing, test_Data, MSE_train_loss, X, scaler, Type, dimension1, dimension2, dimension3, epoch, utilmlab, sess, logger, df_ref, M, Test_No, z_sample, np, AverageWeights, Weights, weightMultiplier):
    print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaahhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")
    if not test_all:
        Z_mb = sample_Z(real_test_No, Dim, z_sample, np)
        M_mb = testM
        X_mb = testX
    else:
        Z_mb = sample_Z(No, Dim, z_sample, np)
        M_mb = Missing
        X_mb = Data
        if fn_ref_csv:
            testX = df_ref[features].values
        else:
            testX = Data
        testM = Missing

        logger.info('testall: {} {} {} {}'.format(
            Z_mb.shape, M_mb.shape, X_mb.shape, New_X_mb.shape))

    print("dimension if M_mb: " + str(len(M_mb)))
    print("dimension if X_mb: " + str(len(X_mb)))
    print("dimension if Z_mb: " + str(len(Z_mb)))

    AverageWeights1 = []

    for i in testX:
            
            mean = 0
            for k in i:
                mean = mean + k
            mean = mean / len(i)

            temp = []
            highThreshold = mean * 1.1
            lowThreshold = mean * 0.9
            for j in i:
                if j < lowThreshold or j > highThreshold:
                    temp.append(5)
                else:
                    temp.append(1)
            AverageWeights1.append(temp)

    New_X_mb = M_mb * X_mb + (1-M_mb) * Z_mb  # Missing Data Introduce
    MSE_final, Sample = sess.run(
        [MSE_test_loss, G_sample],
        feed_dict={X: testX, M: testM, New_X: New_X_mb, Weights: AverageWeights1})
    testX_imputed = Sample # np.where(testM < 1, Sample, testX)

    testX_imputed = scaler.inverse_transform(testX_imputed)
    
    if is_auto_categorical:
        testX_imputed = utilmlab.df_one_hot_to_cat(
            pd.DataFrame(
                testX_imputed,
                columns=prop_df_one_hot['dfcol_one_hot']),
            prop_df_one_hot)

    df_imputed = pd.DataFrame(testX_imputed, columns=features)
    if label is not None:
        df_imputed[[label]] = df[[label]]

    df_imputed.to_csv(fn_ocsv, index=False)
    
    Z_mb = sample_Z(Test_No, Dim, z_sample, np)
    Z_mb_test = sample_Z(real_test_No, Dim, z_sample, np)
    #print("Z_mb_test", Z_mb_test)
    M_mb_test = test_Missing
   #print("M_mb_test", M_mb_test)
    X_mb_test = test_Data
    #print("X_mb_test", X_mb_test)
    testX_test = test_Data
    #print("testX_test", len(testX_test))
    testM_test = test_Missing



    print("DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD")
    print("AverageWeights1", len(AverageWeights1))
    print("testX", len(testX))
    print("test_missing", len(test_Missing))
    print("data", len(Data))
    print("test_data", len(test_Data))

    New_X_test = M_mb_test * X_mb_test + (1-M_mb_test) * Z_mb_test  # Missing Data Introduce
    print("part 1", len(M_mb_test * X_mb_test))
    print("prart 2", len((1-M_mb_test) * Z_mb_test))
    print("New_X_test", len(New_X_test))
    print("tetsM", len(testM))
    MSE_test_data, test_Sample = sess.run([MSE_train_loss, G_sample],
                                 feed_dict={X: testX, M: testM, New_X: New_X_test, Weights: AverageWeights1})


        
   
    
    test_Sample = scaler.inverse_transform(test_Sample)
    
    df_test = pd.DataFrame(test_Sample, columns=features)

    string1 = "accell_y_imputed_test_d1_4n" + "_d2_"+ str(int(dimension2)) + "_d3_"+str(int(dimension3))+"_epoches_"+str(epoch)+".csv"
    string2 = "accell_x_imputed_test_weighted" + str(weightMultiplier) + "_d1_4n" + "_d2_"+ str(int(dimension2)) + "_d3_"+str(int(dimension3))+"_epoches_"+str(epoch)+"_weightMult_" + str(int(weightMultiplier))+".csv"
    string3 = "accell_z_imputed_test_d1_4n" + "_d2_"+ str(int(dimension2)) + "_d3_"+str(int(dimension3))+"_epoches_"+str(epoch)+".csv"
    string4 = "stretch_imputed_test_d1_4n" + "_d2_"+ str(int(dimension2)) + "_d3_"+str(int(dimension3))+"_epoches_"+str(epoch)+".csv"


    if Type == 2:
      df_test.to_csv(string2, index=False)
    if Type == 1:
       df_test.to_csv(string4, index=False)

    if Type == 3:
       df_test.to_csv(string1, index=False)

    if Type == 4:
       df_test.to_csv(string3, index=False)