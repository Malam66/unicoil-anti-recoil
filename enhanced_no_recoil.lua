-- Enhanced No Recoil Lua Script
-- Features: Configurable patterns, sensitivity, multiple weapons
-- Based on the simple script but with advanced functionality

-- Configuration
local config = {
    sensitivity = 1.0,
    recoil_patterns = {
        default = {{0, 5}, {0, 5}, {0, 5}, {0, 5}, {0, 5}},
        strong = {{0, 8}, {1, 8}, {-1, 8}, {0, 8}, {1, 8}},
        weak = {{0, 3}, {0, 3}, {0, 3}, {0, 3}, {0, 3}},
        ak47 = {{0, 6}, {2, 6}, {-2, 6}, {0, 6}, {2, 6}},
        m4a1 = {{0, 4}, {1, 4}, {-1, 4}, {0, 4}, {1, 4}},
        sniper = {{0, 10}, {0, 10}}
    },
    current_pattern = "default",
    delay = 1,
    enabled = true
}

-- Variables
local isActive = false
local currentPattern = config.recoil_patterns[config.current_pattern]

EnablePrimaryMouseButtonEvents(true);

function OnEvent(event, arg)
    -- Toggle script with F1
    if IsKeyLockOn("scrolllock") then
        if not isActive then
            isActive = true
            OutputLogMessage("No Recoil: ENABLED\n")
        end
    else
        if isActive then
            isActive = false
            OutputLogMessage("No Recoil: DISABLED\n")
        end
    end
    
    -- Change pattern with F2
    if event == "MOUSE_BUTTON_PRESSED" and arg == 5 then
        local patterns = {"default", "strong", "weak", "ak47", "m4a1", "sniper"}
        local currentIndex = 1
        for i, pattern in ipairs(patterns) do
            if pattern == config.current_pattern then
                currentIndex = i
                break
            end
        end
        currentIndex = currentIndex % #patterns + 1
        config.current_pattern = patterns[currentIndex]
        currentPattern = config.recoil_patterns[config.current_pattern]
        OutputLogMessage("Pattern: " .. config.current_pattern .. "\n")
    end
    
    -- Adjust sensitivity with F3
    if event == "MOUSE_BUTTON_PRESSED" and arg == 4 then
        config.sensitivity = config.sensitivity + 0.1
        if config.sensitivity > 2.0 then
            config.sensitivity = 0.5
        end
        OutputLogMessage("Sensitivity: " .. string.format("%.1f", config.sensitivity) .. "\n")
    end
    
    -- Main recoil compensation
    if isActive and IsMouseButtonPressed(3) then
        repeat
            if IsMouseButtonPressed(1) then
                repeat
                    -- Apply recoil pattern
                    for i, movement in ipairs(currentPattern) do
                        if not IsMouseButtonPressed(1) then break end
                        
                        local deltaX = math.floor(movement[1] * config.sensitivity)
                        local deltaY = math.floor(movement[2] * config.sensitivity)
                        
                        MoveMouseRelative(deltaX, deltaY)
                        Sleep(config.delay)
                    end
                until not IsMouseButtonPressed(1)
            end
        until not IsMouseButtonPressed(3)
    end
end 