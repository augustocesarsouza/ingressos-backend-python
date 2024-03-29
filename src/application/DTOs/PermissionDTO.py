class PermissionDTO:
    def __init__(self, id, visualName, permissionName) -> None:
        self.Id = id
        self.VisualName = visualName
        self.PermissionName = permissionName

    def to_dict(self):
        return {
            key[0].lower() + key[1:]: value for key, value in vars(self).items() if value is not None
        }
