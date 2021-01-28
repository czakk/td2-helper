import Helper

def test_cmd_generator_kick():
    # given
    parms = ["Kolejarz123","Trolling"]
    choice = "2"
    # when
    result = Helper.cmd_generator(parms,choice)
    # then
    assert result == "/kick_driver Kolejarz123 Trolling"

def test_cmd_generator_sklad():
    #given
    parms = ["im_", "m2","5","10","test"]
    choice = "1"
    # when
    result = Helper.cmd_generator(parms,choice)
    # then
    assert result == "/sp Im_M2:5 n:10,test"

def test_File_Test():
    # given
    file = "sklady_helper.txt"
    file2 = "posterunki_helper.txt"
    # then
    assert Helper.File_test(file).file_exist() != False
    assert Helper.File_test(file2).file_exist() != False
 
