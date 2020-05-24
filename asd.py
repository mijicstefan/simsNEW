def file_clicked(index):
        # print(file_system_model.filePath(index))
        index = tree_view.currentIndex()
        file_clicked_param = os.path.basename(
            file_system_model.filePath(index))