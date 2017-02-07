# This will make it easier to create stuff using GUIs, this will have more things in the future

guiButton = loader.loadModel('phase_3/models/gui/tt_m_gui_mat_mainGui.bam')
btnUp = guiButton.find('**/tt_t_gui_mat_shuffleUp')
btnDn = guiButton.find('**/tt_t_gui_mat_shuffleDown')
btnRlvr = guiButton.find('**/tt_t_gui_mat_shuffleUp')
# Use for buttons: image = (btnUp, btnDn, btnRlvr), image_color = (1, 1, 1, 1), image1_color = (0.8, 0.8, 0, 1), image2_color = (0.15, 0.82, 1.0, 1),

guiButtonClassic = loader.loadModel('phase_3/models/gui/quit_button')
btnUpClassic = guiButtonClassic.find('**/QuitBtn_UP')
btnDnClassic = guiButtonClassic.find('**/QuitBtn_DN')
btnRlvrClassic = guiButtonClassic.find('**/QuitBtn_RLVR')