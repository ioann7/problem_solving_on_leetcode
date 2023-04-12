# Time complexity O(n). Space complexity O(n).
class Solution:
    def simplifyPath(self, path: str) -> str:
        dirs_or_files = []
        for dir_or_file in path.split('/'):
            if dir_or_file == '..':
                dirs_or_files and dirs_or_files.pop()
            elif dir_or_file not in ('.', ''):
                dirs_or_files.append(dir_or_file)
        return '/' + '/'.join(dirs_or_files)
