def merge(parcels, left, mid, right):
    """
    Merge two sorted halves based on priority and deadline.
    """

    left_half = parcels[left:mid + 1]
    right_half = parcels[mid + 1:right + 1]

    i = 0
    j = 0
    k = left

    while i < len(left_half) and j < len(right_half):

        # Compare priority first, then deadline
        if (left_half[i]["priority"], left_half[i]["deadline"]) <= \
           (right_half[j]["priority"], right_half[j]["deadline"]):

            parcels[k] = left_half[i]
            i += 1

        else:
            parcels[k] = right_half[j]
            j += 1

        k += 1

    # Copy remaining elements from left half
    while i < len(left_half):
        parcels[k] = left_half[i]
        i += 1
        k += 1

    # Copy remaining elements from right half
    while j < len(right_half):
        parcels[k] = right_half[j]
        j += 1
        k += 1


def merge_sort(parcels, left, right):
    """
    Recursively sort parcels using Merge Sort.
    """

    if left < right:

        mid = (left + right) // 2

        # Divide the array into two halves
        merge_sort(parcels, left, mid)
        merge_sort(parcels, mid + 1, right)

        # Merge the sorted halves
        merge(parcels, left, mid, right)


def sort_parcels(parcels):
    """
    Sort parcels by priority and delivery deadline.
    """

    if len(parcels) > 1:
        merge_sort(parcels, 0, len(parcels) - 1)

    return parcels
