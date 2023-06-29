class AddManualTEE:

    locatorEmployee = "//a[@href='/employees/3']"
    locatorTimeEntries = "(//ul/li/span[@class='gx-link UserProfile_tab__1yeyY'])[2]"
    locatorManualTimeEntry = "//span[text()='Manual Time Entry']"
    locatorPopUpLocation = "//div[@name='location_id']"
    locatorPopUpSelectShiftType = "//div[@name='location_id']"
    locatorPopUpSelectProgram = "//div[@name='program_id']"
    locatorCalendar = "//div[@class='ant-picker-input ant-picker-input-active']"
    locatorAddEntryTime = "(//button[@class = 'ant-btn ant-btn-lg'])[1]"
    locatorSelectTime = "//input[@name = 'timesArray[1].checked_in_at']"
    locatorDate = "(//div[@class = 'ant-picker-cell-inner'])[4]"
    locatorAddTimeEntry = "(//button[@class = 'ant-btn ant-btn-primary'])[1]"
