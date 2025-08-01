-- Simple No Recoil Lua Script
-- Similar to the script shown in the image
-- Moves mouse down when both middle and left mouse buttons are held

EnablePrimaryMouseButtonEvents(true);

function OnEvent(event, arg)
    if IsMouseButtonPressed(3) then
        repeat
            if IsMouseButtonPressed(1) then
                repeat
                    MoveMouseRelative(0, 5)
                    Sleep(1)
                until not IsMouseButtonPressed(1)
            end
        until not IsMouseButtonPressed(3)
    end
end 