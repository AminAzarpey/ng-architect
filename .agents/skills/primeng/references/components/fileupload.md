# FileUpload (`p-fileupload`)

FileUpload is an advanced uploader with dragdrop support, multi file uploads, auto uploading, progress tracking and validations.

**Import:**

```ts
import { ButtonModule } from "primeng/button";
import { FileUploadModule } from "primeng/fileupload";
import { ToastModule } from "primeng/toast";
import { MessageService } from "primeng/api";
```

## Example

```typescript
import { Component, inject } from "@angular/core";
import { ButtonModule } from "primeng/button";
import { FileUploadModule } from "primeng/fileupload";
import { ToastModule } from "primeng/toast";
import { MessageService } from "primeng/api";

interface UploadEvent {
  originalEvent: Event;
  files: File[];
}

@Component({
  template: `
    <p-toast />
    <div class="card flex flex-wrap gap-6 items-center justify-between">
      <p-fileupload
        #fu
        mode="basic"
        chooseLabel="Choose"
        chooseIcon="pi pi-upload"
        name="demo[]"
        url="https://www.primefaces.org/cdn/api/upload.php"
        accept="image/*"
        maxFileSize="1000000"
        (onUpload)="onUpload($event)"
      />
      <p-button label="Upload" (onClick)="fu.upload()" severity="secondary" />
    </div>
  `,
  standalone: true,
  imports: [ButtonModule, FileUploadModule, ToastModule],
  providers: [MessageService],
})
export class FileuploadBasicDemo {
  private messageService = inject(MessageService);
}
```

## Inputs

| Name                           | Type                     | Default                           | Description                                                                                                                                                                       |
| ------------------------------ | ------------------------ | --------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| name                           | string                   | -                                 | Name of the request parameter to identify the files at backend.                                                                                                                   |
| url                            | string                   | -                                 | Remote url to upload the files.                                                                                                                                                   |
| method                         | "post" \| "put"          | post                              | HTTP method to send the files to the url such as "post" and "put".                                                                                                                |
| multiple                       | boolean                  | false                             | Used to select multiple files at once from file dialog.                                                                                                                           |
| accept                         | string                   | -                                 | Comma-separated list of pattern to restrict the allowed file types. Can be any combination of either the MIME types (such as "image/\*") or the file extensions (such as ".jpg"). |
| disabled                       | boolean                  | false                             | Disables the upload functionality.                                                                                                                                                |
| auto                           | boolean                  | false                             | When enabled, upload begins automatically after selection is completed.                                                                                                           |
| withCredentials                | boolean                  | false                             | Cross-site Access-Control requests should be made using credentials such as cookies, authorization headers or TLS client certificates.                                            |
| maxFileSize                    | number                   | -                                 | Maximum file size allowed in bytes.                                                                                                                                               |
| invalidFileSizeMessageSummary  | string                   | {0}: Invalid file size,           | Summary message of the invalid file size.                                                                                                                                         |
| invalidFileSizeMessageDetail   | string                   | maximum upload size is {0}.       | Detail message of the invalid file size.                                                                                                                                          |
| invalidFileTypeMessageSummary  | string                   | {0}: Invalid file type,           | Summary message of the invalid file type.                                                                                                                                         |
| invalidFileTypeMessageDetail   | string                   | allowed file types: {0}.          | Detail message of the invalid file type.                                                                                                                                          |
| invalidFileLimitMessageDetail  | string                   | limit is {0} at most.             | Detail message of the invalid file type.                                                                                                                                          |
| invalidFileLimitMessageSummary | string                   | Maximum number of files exceeded, | Summary message of the invalid file type.                                                                                                                                         |
| style                          | { [klass: string]: any } | -                                 | Inline style of the element.                                                                                                                                                      |
| styleClass                     | string                   | -                                 | Class of the element.                                                                                                                                                             |
| previewWidth                   | number                   | 50                                | Width of the image thumbnail in pixels.                                                                                                                                           |
| chooseLabel                    | string                   | -                                 | Label of the choose button. Defaults to PrimeNG Locale configuration.                                                                                                             |
| uploadLabel                    | string                   | -                                 | Label of the upload button. Defaults to PrimeNG Locale configuration.                                                                                                             |
| cancelLabel                    | string                   | -                                 | Label of the cancel button. Defaults to PrimeNG Locale configuration.                                                                                                             |
| chooseIcon                     | string                   | -                                 | Icon of the choose button.                                                                                                                                                        |
| uploadIcon                     | string                   | -                                 | Icon of the upload button.                                                                                                                                                        |
| cancelIcon                     | string                   | -                                 | Icon of the cancel button.                                                                                                                                                        |
| showUploadButton               | boolean                  | true                              | Whether to show the upload button.                                                                                                                                                |
| showCancelButton               | boolean                  | true                              | Whether to show the cancel button.                                                                                                                                                |
| mode                           | "advanced" \| "basic"    | advanced                          | Defines the UI of the component.                                                                                                                                                  |
| headers                        | HttpHeaders              | -                                 | HttpHeaders class represents the header configuration options for an HTTP request.                                                                                                |
| customUpload                   | boolean                  | false                             | Whether to use the default upload or a manual implementation defined in uploadHandler callback. Defaults to PrimeNG Locale configuration.                                         |
| fileLimit                      | number                   | -                                 | Maximum number of files that can be uploaded.                                                                                                                                     |
| uploadStyleClass               | string                   | -                                 | Style class of the upload button.                                                                                                                                                 |
| cancelStyleClass               | string                   | -                                 | Style class of the cancel button.                                                                                                                                                 |
| removeStyleClass               | string                   | -                                 | Style class of the remove button.                                                                                                                                                 |
| chooseStyleClass               | string                   | -                                 | Style class of the choose button.                                                                                                                                                 |
| chooseButtonProps              | ButtonProps              | -                                 | Used to pass all properties of the ButtonProps to the choose button inside the component.                                                                                         |
| uploadButtonProps              | ButtonProps              | ...                               | Used to pass all properties of the ButtonProps to the upload button inside the component.                                                                                         |
| cancelButtonProps              | ButtonProps              | ...                               | Used to pass all properties of the ButtonProps to the cancel button inside the component.                                                                                         |

## Outputs

| Name                 | Parameters                     | Description                                                                                                                                                                 |
| -------------------- | ------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| onBeforeUpload       | event: FileBeforeUploadEvent   | Callback to invoke before file upload is initialized.                                                                                                                       |
| onSend               | event: FileSendEvent           | An event indicating that the request was sent to the server. Useful when a request may be retried multiple times, to distinguish between retries on the final event stream. |
| onUpload             | event: FileUploadEvent         | Callback to invoke when file upload is complete.                                                                                                                            |
| onError              | event: FileUploadErrorEvent    | Callback to invoke if file upload fails.                                                                                                                                    |
| onClear              | event: Event                   | Callback to invoke when files in queue are removed without uploading using clear all button.                                                                                |
| onRemove             | event: FileRemoveEvent         | Callback to invoke when a file is removed without uploading using clear button of a file.                                                                                   |
| onSelect             | event: FileSelectEvent         | Callback to invoke when files are selected.                                                                                                                                 |
| onProgress           | event: FileProgressEvent       | Callback to invoke when files are being uploaded.                                                                                                                           |
| uploadHandler        | event: FileUploadHandlerEvent  | Callback to invoke in custom upload mode to upload the files manually.                                                                                                      |
| onImageError         | event: Event                   | This event is triggered if an error occurs while loading an image file.                                                                                                     |
| onRemoveUploadedFile | event: RemoveUploadedFileEvent | This event is triggered if an error occurs while loading an image file.                                                                                                     |

## Templates

| Name       | Type                                            | Description                  |
| ---------- | ----------------------------------------------- | ---------------------------- |
| file       | TemplateRef<void>                               | Custom file template.        |
| header     | TemplateRef<FileUploadHeaderTemplateContext>    | Custom header template.      |
| content    | TemplateRef<FileUploadContentTemplateContext>   | Custom content template.     |
| toolbar    | TemplateRef<void>                               | Custom toolbar template.     |
| chooseicon | TemplateRef<void>                               | Custom choose icon template. |
| filelabel  | TemplateRef<FileUploadFileLabelTemplateContext> | Custom file label template.  |
| uploadicon | TemplateRef<void>                               | Custom upload icon template. |
| cancelicon | TemplateRef<void>                               | Custom cancel icon template. |
| empty      | TemplateRef<void>                               | Custom empty state template. |

## Methods

| Name               | Parameters                  | Return Type | Description                 |
| ------------------ | --------------------------- | ----------- | --------------------------- |
| uploader           |                             | void        | Uploads the selected files. |
| clear              |                             | void        | Clears the files list.      |
| remove             | event: Event, index: number | void        | Removes a single file.      |
| removeUploadedFile | index: number               | void        | Removes uploaded file.      |

**Full API & more examples:** https://primeng.org/fileupload
